from moviepy.editor import *
from scipy.io import wavfile


def Convert(inputpath):
    listdir = os.listdir(inputpath)
    mp4__list = [name for name in listdir if name.endswith('.mp4')]
    for file in mp4__list:

        filepath = os.path.join(inputpath, file)
        video = VideoFileClip(filepath)
        list_filepath = list(filepath)
        if list_filepath[-1] == '4':
            Typee = input('Please Enter Type: mp3 or wav: ')
            if Typee == 'mp3':
                list_filepath[-1] = '3'
                filepath = ''.join(list_filepath)
                c = filepath.split('/')[-1]
                if c in listdir:
                    print(c, 'Is Already Exist')
                    continue
                else:
                    filepath = ''.join(list_filepath)
                    print(filepath)
                    audio = video.audio
                    audio.write_audiofile(filepath)
                    Cut_check = input('Need a cutter? (yes/no) : ')
                    if Cut_check == 'yes':
                        Hz = int(input('Please input Sample Frequency(Hz): '))
                        Start_point = int(input('Input Start Point(s): '))
                        End_point = int(input('Input End Point(s): '))
                        like = wavfile.read(filepath)
                        wavfile.write(filepath, Hz, like[1][Start_point * Hz: End_point * Hz])
                        print('Finished!')

                    else:
                        print('Finished!')

            elif Typee == 'wav':
                list_filepath[-3] = 'w'
                list_filepath[-2] = 'a'
                list_filepath[-1] = 'v'
                filepath = ''.join(list_filepath)
                c = filepath.split('/')[-1]
                if c in listdir:
                    print(c, 'Is Already Exist')
                    continue
                else:
                    print(filepath)
                    audio = video.audio
                    audio.write_audiofile(filepath)
                    Cut_check = input('Need a cutter? (yes/no) : ')
                    if Cut_check == 'yes':
                        Hz = int(input('Please input Sample Frequency(Hz): '))
                        Start_point = int(input('Input Start Point(s): '))
                        End_point = int(input('Input End Point(s): '))
                        like = wavfile.read(filepath)
                        wavfile.write(filepath, Hz, like[1][Start_point * Hz: End_point * Hz])
                        print('Finished!')

                    else:
                        print('Finished!')
            else:
                print('Sorry,Cant do that.(Only support mp3/wav)')
                break
        else:
            print('Found None .mp4 file.')
    print('All Finished!')



if __name__ == '__main__':
    vediopath = input('Enter File Path: ')
    if len(vediopath) < 1 :
        vediopath = '/Users/zireael19andre/Movies/TubeGet'
    Convert(vediopath)
