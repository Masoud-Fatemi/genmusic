#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:08:44 2024

@author: masoud
"""

import os
import librosa
import soundfile as sf

# Directory containing MP3 files
mp3_directory = 'mp3/'
wav_directory = 'wav/'
sampling_rate = 16000  # Set your desired sampling rate

if not os.path.exists(wav_directory):
    os.makedirs(wav_directory)

# Iterate over all MP3 files
for filename in os.listdir(mp3_directory):
    if filename.endswith('.mp3'):
        
        file_path = os.path.join(mp3_directory, filename)
        # Load the MP3 file
        audio, _ = librosa.load(file_path, sr=sampling_rate, mono=True)
        # Define new filename for the WAV file
        wav_filename = os.path.splitext(filename)[0] + '.wav'
        wav_path = os.path.join(wav_directory, wav_filename)
        # Save the file in WAV format
        sf.write(wav_path, audio, samplerate=sampling_rate)
        print(f'Processed and saved: {wav_filename}')
