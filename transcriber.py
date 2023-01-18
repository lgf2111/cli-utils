#!/usr/bin/env python3

import whisper
import os
import sys


def get_videos_path():
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        return input("Enter the path to the videos: ")


def get_output_path():
    if len(sys.argv) >= 3:
        return sys.argv[2]
    else:
        return input("Enter the path to the output: ")


def get_video_fns(videos_path):
    fns = os.listdir(videos_path)
    video_fns = [fn for fn in fns if fn.endswith(".mp4")]
    return video_fns


def get_text_from_video(video_path):
    result = model.transcribe(video_path, verbose=True)
    result_text = result["text"]
    return result_text


def save_text_to_file(text, output_path):

    with open(os.path.join(output_path, video_fn.replace(".mp4", ".txt")), "w") as f:
        f.write(text)


if __name__ == "__main__":
    model = whisper.load_model("tiny.en")
    videos_path = get_videos_path()
    output_path = get_output_path()
    video_fns = get_video_fns(videos_path)
    for video_fn in video_fns:
        result_text = get_text_from_video(os.path.join(videos_path, video_fn))
        save_text_to_file(result_text, output_path)
