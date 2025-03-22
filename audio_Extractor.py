import moviepy.editor

cvt_video = moviepy.editor.VideoFileClip("video.mp4")

ext_audio = cvt_video.audio

ext_audio.write_audiofile("audio_Extracted.mp3")