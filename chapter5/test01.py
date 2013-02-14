def read_player(player_filename):
    ''' read "player_filename" file and remove new line character and split items by , '''
    retValue = []
    try:
        with open(player_filename) as player :
            origSrc = player.readline()
            retValue = origSrc.strip().split(',')
        return retValue
    except IOError as err:
        print('File Error :' + str(err))

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
        (mins, secs) = time_string.split(splitter)
    elif ':' in time_string:
        splitter = ':'
        (mins, secs) = time_string.split(splitter)
    else:
        return(time_string)
    return mins + '.' + secs
