def plusOne(arr):
    for i, j in enumerate(arr):
        arr[i] = j + 1

def main():
    testArr = [25, 12, 64, 12]
    plusOne(testArr)
    print(testArr)

if __name__ == '__main__':
    main()
#changes