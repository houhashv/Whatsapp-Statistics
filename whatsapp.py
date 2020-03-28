# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:40:53 2018
@author: yossi hohashvili
"""
import pandas as pd
import re


def get_data(path):
    with open(path, encoding="utf-8") as file:
        data = []
        for line in file:
            search = re.search("(\d{1,2}).(\d{1,2}).(\d{4})," + \
                               " (\d{1,2}):(\d{2}):(\d{2})", line)
            line = line[:-1].split(':')
            if len(line) >= 4:
                sender = line[2][4:]
                message = ":".join(line[3:])
                row = [x for x in search.groups()] + [sender, message, len(message)]
                if "<‏התמונה הושמטה>" in message:
                    row += [1, 0, 0, 0]
                elif " <‏קטע קול הושמט>" in message:
                    row += [0, 1, 0, 0]
                elif " <‏הסרט הושמט>" in message:
                    row += [0, 0, 1, 0]
                elif "<‏GIF הושמט>" in message:
                    row += [0, 0, 0, 1]
                else:
                    row += [0, 0, 0, 0]
                data.append(row)

    df = pd.DataFrame(data, columns=["day", "month", \
                                     "year", "hour", "minute", "second", \
                                     "sender", "message", "chars", \
                                     "pic", "voice", "video", "gif"])
    return df


def chars_stats(df):
    return df.groupby("sender").agg({"chars": ["count", "sum", "mean"]})

def pic_stats(df):
    return df.groupby("sender").agg({"pic": ["count", "sum", "mean"]})


def voice_stats(df):
    return df.groupby("sender").agg({"voice": ["count", "sum", "mean"]})


def video_stats(df):
    return df.groupby("sender").agg({"video": ["count", "sum", "mean"]})


def gif_stats(df):
    return df.groupby("sender").agg({"gif": ["count", "sum", "mean"]})


def response_hist(df, name):
    df[df["sender"] != name].sort_values("hour")["hour"].hist()


def response_hist_name(df, name):
    df[df["sender"] == name].sort_values("hour")["hour"].hist()


if __name__ == "__main__":

    path = "D:\Google Drive\Data\שיחות ווטסאפ\WhatsApp Chat - ניסים אחי\\_chat.txt"
    df = get_data(path)
    print(chars_stats(df))
    print(pic_stats(df))
    print(voice_stats(df))
    print(video_stats(df))
    print(gif_stats(df))
