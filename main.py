import re

if __name__ == '__main__':
    pattern = r'205.189.154.54.+01/Jul/1995.+GET.+txt.+200'
    #                     server id          date       get a file   .txt   success
    with open("access_log_Jul95", 'rb') as file:
        out = []
        for line in file:
            if re.search(pattern, str(line)):
                print(line[:-1])