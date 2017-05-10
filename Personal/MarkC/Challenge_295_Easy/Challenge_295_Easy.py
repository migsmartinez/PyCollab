def challenge295(strA: str, strB: str) -> None:
    #always print the original first argument
    print(strA)

    #testing enumeration by zipped strings just for fun
    for i, v in enumerate(zip(strA, strB)):
        #do not print if chars in the same position are the same
        if (v[0] != v[1]):
            #testing separator option for printing
            print(strB[:i + 1], strA[i + 1:], sep = '')

if __name__ == "__main__":
    import sys

    challenge295(sys.argv[1], sys.argv[2])
