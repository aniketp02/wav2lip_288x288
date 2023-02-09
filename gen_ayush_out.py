import os
import subprocess

audio_files = os.listdir('ayushman_kurana/audios/')
video_files = os.listdir('ayushman_kurana/man_videos/')
checkpoint_path = 'checkpoints/wav2lip/checkpoint_step000186000.pth' #--> results1
# 'checkpoints/visual/checkpoint_step000205000.pth' # --> results_visual

#'checkpoints/best_288x288.pth' --> results

print(audio_files)
print(video_files)

for video in video_files:
    video_path = os.path.join('ayushman_kurana/man_videos/', video)
    vcode = video.split('.')[0][-1]
    for audio in audio_files:
        audio_path = os.path.join('ayushman_kurana/audios/', audio)
        acode = audio.split('.')[0][-1]

        out_name = 'out' + vcode + acode + '.mp4'
        out_path = os.path.join('ayushman_kurana/man_outputs/', out_name)

        cmd = f'python3 inference.py --checkpoint_path {checkpoint_path} --face {video_path} --audio {audio_path} --outfile {out_path}'
        print(cmd)
        subprocess.call(cmd, shell=True)
