import re
def pretty_print(main_Dic, data):
    print ("[{'",end="")
    for key in main_Dic:
        if (key == 'action'):
            print (key + "' : '" + main_Dic[key] + "',\n",end="")
    if(len(data)>1):
        for d in data[:-1]:
            print("  'data': {",end="")
            for key in d:
                print("'" + key + "': '" + d[key] + "',\n",end="")
            print ("},\n",end="")
    else:
        for d in data:
            print("  'data': {",end="")
            for key in d:
                print("'" + key + "': '" + d[key] + "',\n",end="")
            print ("},\n",end="")
    for key in main_Dic:
        if (key != 'action'):
            print ("'" + key + "': '" + main_Dic[key] + "',\n",end="")
    print('}]\n',end="")


def main():
    main_Dic = {}
    data = [{}]
    cnt = 0
    file = open('Logfile.txt', 'r')
    for i, line in enumerate(file.readlines()):

        if (line.find('}') == 0 and line.find('};') == -1):
            cnt = cnt + 1
            data.append({})
        if (len(re.findall('\\bset\\b', line)) == 1):
            main_Dic['action'] = 'set'
            main_Dic['subtype'] = line.split(' ')[1].split('(')[1].strip('\n').strip('\r').strip('{').strip(')')
            main_Dic['type'] = line.split(' ')[1].split('(')[0]
        if (line.find('{\n') != -1):
            continue
        if (line.find('-') != -1):
            key = line.split('-')[1].split(' ')[0].strip('-').strip('\t')
            value = line.split('-')[1].split(' ', 1)[1].strip('{').strip('\n').strip('\r').strip('}')
            data[cnt][key] = value
        if (line.find('};\n') != -1):
            cnt = 0
            pretty_print(main_Dic, data)
            main_Dic = {}
            data = [{}]



if __name__ == '__main__':
    main()


