import os;
from pathlib import Path;
import time;
from wit import Wit;

def main():

    # get directories
    parentDir = str(Path(os.getcwd()));
    audioDir = parentDir + '/test_audio';

    # open logs
    log = open("results.txt", "w");
    empty = open("empty.txt", "w")

    i = 0;
    numEmpty = 0;

    # init Wit, access token for wit.ai found in app settings
    access_token = "DFKCCZXCNSMCOLOGG5GVUGQIOFTE45SG";
    client = Wit(access_token);

    # for each wav file, open and convert to text using Wit.AI
    for wav in os.listdir(audioDir):
        i = i + 1;
        print('Reading file ' + str(i));
        log.write(str(i) + ". Result of STT for " + wav + ": \nText:");

        with open(audioDir + '/' + wav, 'rb') as w:
            try:
                resp = client.speech(w, None, {'Content-Type': 'audio/wav'});
            except:
                print('Too many requests. Program exiting.');
                break;
            if (i % 50 == 0):
                print("Sleeping to avoid excess requests...")
                time.sleep(40);

        # if response text is empty (ie. could not interpret speech)
        if (resp.get('_text') == ''):
            numEmpty = numEmpty + 1;
            empty.write(str(numEmpty) + '. ' + audioDir + '/' + wav + '\n');

        log.write("\"" + resp.get('_text') + "\"");
        log.write("\n\n");

    print('Total number of files read: ' + str(i));
    print('Number of empty responses (ie. could not interpret): ' + str(numEmpty));

    log.write('Total number of files read: ' + str(i));
    log.write('\nNumber of empty responses (ie. could not interpret): ' + str(numEmpty));

    empty.close();
    log.close();


    # interactive mode
    #client.interactive();

if __name__ == "__main__":
    main();
