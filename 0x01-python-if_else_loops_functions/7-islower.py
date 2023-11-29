#!/usr/bin/python3
def lo_wer(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False

if __name__ == '__main__':
    print(lo_wer('C'))
