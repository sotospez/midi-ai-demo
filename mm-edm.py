import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

# Set tempo (in BPM)
tempo = 128  # Typical tempo for Big Room House / EDM

# Create a new MIDI file
mid = MidiFile()

# Create tracks for the different elements of the track
tracks = [MidiTrack() for _ in range(10)]
for i, track in enumerate(tracks):
    track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    mid.tracks.append(track)

# Track 0: Kick drum (simple 4/4 beat)
for i in range(16):
    if i % 4 == 0:  # Kick on each beat
        tracks[0].append(Message('note_on', note=36, velocity=64, time=0, channel=9))
        tracks[0].append(Message('note_off', note=36, velocity=64, time=480, channel=9))

# Track 1: Hi-hats (8th notes)
for i in range(32):
    tracks[1].append(Message('note_on', note=42, velocity=64, time=0, channel=9))
    tracks[1].append(Message('note_off', note=42, velocity=64, time=240, channel=9))

# Track 2: Snare drum (on 2nd and 4th beats)
for i in range(16):
    if i % 4 == 2:  # Snare on 2nd and 4th beats
        tracks[2].append(Message('note_on', note=38, velocity=64, time=0, channel=9))
        tracks[2].append(Message('note_off', note=38, velocity=64, time=480, channel=9))

# Track 3: Bassline (simple quarter notes)
bassline_notes = [48, 48, 50, 50, 53, 53, 50, 50]  # C, C, D, D, G, G, D, D
for i in range(8):
    tracks[3].append(Message('note_on', note=bassline_notes[i], velocity=64, time=0, channel=3))
    tracks[3].append(Message('note_off', note=bassline_notes[i], velocity=64, time=960, channel=3))

# Tracks 4-6: Synth melody
melody_notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
for i in range(8):
    for j in range(4, 7):
        tracks[j].append(Message('note_on', note=melody_notes[i], velocity=64, time=0, channel=j))
        tracks[j].append(Message('note_off', note=melody_notes[i], velocity=64, time=480, channel=j))

# Save the MIDI file
mid.save('EDM_style.mid')


# In this script:
#
# Track 0 (channel 0) plays a simple 4/4 kick drum beat.
# Track 1 (channel 1) plays 8th note hi-hats.
# Track 2 (channel 2) plays a snare drum on the 2nd and 4th beats.
# Track 3 (channel 3) plays a simple quarter note bassline.
# Tracks 4-6 (channels 4-6) each play a simple melody using the C major scale.
# This should result in a 10-track MIDI file with a simple beat, bassline, and melody. The file will be saved as 'EDM_style.mid'.
