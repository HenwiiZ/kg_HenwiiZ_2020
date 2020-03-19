import sys

def exist_matching(s1, s2):
    """
    Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
    :param s1: String 1
    :param s2: String 2
    :return: Whether the mapping exists(True or False)
    """
    if (len(s1) != len(s2)):
        return False

    mapping = {}

    #Check character of s1 and s2 one by one
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