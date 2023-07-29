import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

# Set tempo (in microseconds per beat)
tempo = mido.bpm2tempo(120)

# Create a new MIDI file
mid = MidiFile(type=1)


# Create a track for the drum
track_drums = MidiTrack()

mid.tracks.append(track_drums)

# Define drum patterns
kick_pattern = [1, 0, 1, 0, 1, 0, 1, 0] # Kick drum on every beat
snare_pattern = [0, 0, 1, 0, 0, 0, 1, 0] # Snare drum on beats 2 and 4
hihat_pattern = [0, 1, 0, 1, 0, 1, 0, 1] # Hi-hat on the off-beats

# Define MIDI note numbers for the drum parts
kick_note = 36
snare_note = 38
hihat_note = 42



track_drums.append(MetaMessage(type='instrument_name', name='Drum kit'))
track_drums.append(MetaMessage(type='device_name', name='Drum kit'))
# Add drum patterns to the drum track, set channel to 15 (16th channel)
for i in range(32):  # Repeat the pattern for 32 beats
    if kick_pattern[i % len(kick_pattern)]:
        track_drums.append(Message('note_on', note=kick_note, velocity=64, time=0, channel=9 ))
        track_drums.append(Message('note_off', note=kick_note, velocity=64, time=480, channel=9))
    if snare_pattern[i % len(snare_pattern)]:
        track_drums.append(Message('note_on', note=snare_note, velocity=64, time=0, channel=9))
        track_drums.append(Message('note_off', note=snare_note, velocity=64, time=480, channel=9))
    if hihat_pattern[i % len(hihat_pattern)]:
        track_drums.append(Message('note_on', note=hihat_note, velocity=64, time=0, channel=9))
        track_drums.append(Message('note_off', note=hihat_note, velocity=64, time=480, channel=9))

# Create a track for the piano
track_piano = MidiTrack()
mid.tracks.append(track_piano)

# Define a chord progression (Cm, Gm, Ab, Bb)
chords = [[60, 63, 67], [55, 58, 62], [56, 60, 63], [58, 62, 65]]

# Add chords to the piano track, set channel to 1 (2nd channel)
for chord in chords:
    for note in chord:
        track_piano.append(Message('note_on', note=note, velocity=64, time=0, channel=1))
    for note in chord:
        track_piano.append(Message('note_off', note=note, velocity=64, time=1920, channel=1))  # Hold each chord for one measure

# Save the MIDI file
mid.print_tracks()
mid.save('club_dance_beat.mid')


# This script creates a MIDI file named 'club_dance_beat.mid' with a basic club dance beat at 120 BPM in a 4/4 time signature.
# It includes a drum track with a kick drum on every beat, a snare on the second and fourth beats, and hi-hats on the off-beats.
# The piano track plays a simple chord progression (Cm, Gm, Ab, Bb) that changes every measure.
# The velocity (volume) for all notes is set to a moderate level (64).

