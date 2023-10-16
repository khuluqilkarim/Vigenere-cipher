import argparse

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encodeText(string, key):
    temporaryEncode = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        temporaryEncode.append(chr(x))
    return "".join(temporaryEncode)

def decodeText(string, key):
    temporaryDecode = []
    for i in range(len(string)):
        x = (ord(string[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        temporaryDecode.append(chr(x))
    return "".join(temporaryDecode)

def main():
    parser = argparse.ArgumentParser(description="Penggunaan : Vigenère cipher")
    parser.add_argument("-t", "--text", type=str, required=True, help="String yang akan di Enkripsi dan Dekripsi")
    parser.add_argument("-k", "--key", type=str, required=True, help="Key dari Enkripsi dan Dekripsi")
    parser.add_argument("-d", "--decode", action="store_true", default=False, help="Dekripsi Text")
    parser.add_argument("-e", "--encrypt", action="store_true", default=False, help="Enkripsi Text")

    args = parser.parse_args()

    if args.text is not None and args.key is not None:
        if args.encrypt:
            key = generateKey(args.text, args.key)
            print(key)
            temporaryText = encodeText(args.text, key)
            print(f"Encode: {temporaryText}")
        elif args.decode:
            key = generateKey(args.text, args.key)
            print(f"Decode: {decodeText(args.text, key)}")

if __name__ == "__main__":
    main()
