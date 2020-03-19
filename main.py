import sys

def exist_matching(s1, s2):
    if (len(s1) != len(s2)):
        return False

    mapping = {}
    for i in range(len(s1)):
        if s1[i] not in mapping.keys():
            mapping[s1[i]] = s2[i]
        else:
            if mapping[s1[i]] != s2[i]:
                return False

    return True

def main():
    print(exist_matching(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
    main()