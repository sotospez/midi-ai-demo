import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

# Set tempo (in BPM)
tempo = 256

# Create a new MIDI file
mid = MidiFile()

# Create a new MIDI file
mid = MidiFile()

# Create a track for the drum
track_drums = MidiTrack()

track_drums.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

mid.tracks.append(track_drums)

# Define drum patterns
kick_pattern = [1, 0, 1, 0, 1, 0, 1, 0] * 4 + [1, 0, 1, 0, 1, 1, 1, 0] * 4  # Adding variation to the kick pattern
snare_pattern = [0, 0, 1, 0, 0, 0, 1, 0] * 8  # Keeping the snare pattern the same
hihat_pattern = [0, 1, 0, 1, 0, 1, 0, 1] * 8  # Keeping the hi-hat pattern the same

# Define MIDI note numbers for the drum parts
kick_note = 36
snare_note = 38
hihat_note = 42

# Add drum patterns to the drum track, set channel to 15 (16th channel)
for i in range(160):  # Repeat the pattern for 64 beats
    if kick_pattern[i % len(kick_pattern)]:
        track_drums.append(Message('note_on', note=kick_note, velocity=64, time=0, channel=9))
        track_drums.append(Message('note_off', note=kick_note, velocity=64, time=480, channel=9))
    if snare_pattern[i % len(snare_pattern)]:
        track_drums.append(Message('note_on', note=snare_note, velocity=64, time=0, channel=9))
        track_drums.append(Message('note_off', note=snare_note, velocity=64, time=480, channel=9))
    if hihat_pattern[i % len(hihat_pattern)]:
        track_drums.append(Message('note_on', note=hihat_note, velocity=64, time=0, channel=9))
        track_drums.append(Message('note_off', note=hihat_note, velocity=64, time=480, channel=9))

# Create a track for the piano
track_piano = MidiTrack()
track_piano.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
mid.tracks.append(track_piano)

# Define two chord progressions and alternate between them
chords1 = [[60, 63, 67], [55, 58, 62], [56, 60, 63], [58, 62, 65]]  # Cm, Gm, Ab, Bb
chords2 = [[60, 64, 67], [55, 59, 62], [57, 61, 64], [59, 63, 66]]  # C, G, D, A

# Add chords to the piano track, set channel to 1 (2nd channel)
for i in range(4):  # Repeat the progression for 8 measures
    chords = chords1 if i % 2 == 0 else chords2  # Alternate between the two chord progressions
    for chord in chords:
        for note in chord:
            track_piano.append(Message('note_on', note=note, velocity=64, time=0, channel=0))
        for note in chord:
            track_piano.append(
                Message('note_off', note=note, velocity=64, time=1920, channel=0))  # Hold each chord for one measure

# Create a track for the guitar
track_guitar = MidiTrack()
track_guitar.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
mid.tracks.append(track_guitar)

# Define two chord progressions and create an arpeggio pattern
# chords1 = [[60, 63, 67], [55, 58, 62], [56, 60, 63], [58, 62, 65]]  # Cm, Gm, Ab, Bb
# chords2 = [[60, 64, 67], [55, 59, 62], [57, 61, 64], [59, 63, 66]]  # C, G, D, A
# Define two chord progressions with 7th and 9th chords and create an arpeggio pattern
chords1 = [[60, 63, 67, 70], [55, 58, 62, 65], [56, 60, 63, 66], [58, 62, 65, 68]]  # Cm7, Gm7, AbMaj7, BbMaj7
chords2 = [[60, 64, 67, 70], [55, 59, 62, 66], [57, 61, 64, 67], [59, 63, 66, 69]]  # CMaj7, GMaj9, DMaj7, AMaj9

# Add arpeggios to the guitar track, set channel to 2 (3rd channel)
for i in range(4):  # Repeat the progression for 8 measures
    chords = chords1 if i % 2 == 0 else chords2  # Alternate between the two chord progressions
    for chord in chords:
        for note in chord:
            track_guitar.append(Message('note_on', note=note, velocity=64, time=0, channel=10))
            track_guitar.append(
                Message('note_off', note=note, velocity=64, time=480, channel=10))  # Play each note for a beat

mid.print_tracks()
# Save the MIDI file
mid.save('club_dance_beat2.mid')


#  This script adds a guitar track to the MIDI file on channel 3
#  The guitar part is an arpeggio pattern that follows the chord progression.
#  Each note of the chord is played for a beat.
#  The chord progressions alternate every measure, just like in the piano part.