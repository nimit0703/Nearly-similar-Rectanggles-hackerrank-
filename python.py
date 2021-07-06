def getCount(rows, columns, A):
    
    res = 0

    for i in range(rows):
        for j in range(i + 1, rows, 1):
            if (A[i][0] * A[j][1] ==
                A[i][1] * A[j][0]):
                res += 1
                
    return res


if __name__ == '__main__':
    
    rows = int(input())
    columns = int(input())
    A=list()
    for i in range(rows):
        A.append(list(map(int,input().split(' ',columns-1))))

    print(getCount(rows, columns, A))
