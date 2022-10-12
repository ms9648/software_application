import ujson
import pandas as pd
import numpy as np
import tqdm

def get_frequency_vector(playlist_id, all_playlist):
    df = pd.DataFrame()
    
    for song in tqdm.tqdm_notebook(all_playlist.loc[playlist_id, 'tracks'].index):
        for other_playlist in all_playlist.drop(1, axis = 0).index:
            if song in all_playlist['tracks'][other_playlist].index:
                frequency_vector = pd.DataFrame(all_playlist['tracks'][other_playlist].index)
                df = pd.concat([df, frequency_vector[frequency_vector != song]])

    return df.value_counts()