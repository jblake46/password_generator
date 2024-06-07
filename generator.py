import random
def passwordGenerator():
    #gives number of characters
    numChars = random.randint(5,9)
    numDigits = random.randint(3, 7)
    numSymbols = random.randint(2,5)

    #list of symbols
    special_characters = ['!', '#', '$', '&']

    char = ''
    charList = []
    for i in range(numChars):
        lowerCaser = random.randint(0,1)
        if lowerCaser == 0:
           char = (chr(random.randint(65,90)))
           charList.append(char.lower())
        else:
            charList.append(chr(random.randint(65,90)))
        
    numList = []
    for i in range(numDigits):
        numList.append((random.randint(0,9)))
    char_list = [str(i) for i in numList]
    symbolList = []
    for i in range(numSymbols):
        random_special_char = random.randint(0,2)
        symbolList.append(special_characters[random_special_char])

    password = ''.join(charList) + ''.join(char_list) + ''.join(symbolList)
    tmp = ''.join(password)
    #random.shuffle(tmpList)
    #password = ''.join(tmpList)
    print(password)
    return password
def jumbler(passwordStr):
    tmp = list(passwordStr)
    random.shuffle(tmp)
    print(''.join(tmp))
    return ''.join(tmp)
def main():

    print("Hello, World!")
    password = passwordGenerator()
    jumbler1 = jumbler(password)
    with open('file.txt', 'a') as f:
        f.write(password + '\n')


if __name__ == "__main__":
    main()
