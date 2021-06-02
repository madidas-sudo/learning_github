import mathFunctions as mf

def main():
    testArr = [25, 12, 64, 12]

    mf.plusOne(testArr)
    print(testArr)

    mf.divideByfour(testArr)
    print(testArr)

    mf.plusThree(testArr)
    print(testArr)

    mf.flatten(testArr)
    print(testArr)

    mf.plusTwo(testArr)
    print(testArr)

if __name__ == '__main__':
    main()
