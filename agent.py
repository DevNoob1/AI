def clean(floor): 
    i, j, row, col = 0, 0, len(floor), len(floor[0])
    for i in range(row):
        if(i%2 == 0):
            for j in range(col):
                if(floor[i][j] == 1):
                    print_F(floor, i, j)
                    floor[i][j] = 0
                print_F(floor, i, j)
        else:
            for j in range(col-1, -1, -1):
                if(floor[i][j] == 1):
                    print_F(floor, i, j)
                    floor[i][j] = 0
                print_F(floor, i, j)
def print_F(floor, row, col): 
    
    print("The Floor matrix is as below:")
    for r in range(len(floor)):
        for c in range(len(floor[r])):
            if r == row and c == col:
                print(f" >{floor[r][c]}< ", end = '')
            else:
                print(f"  {floor[r][c]}  ", end = '')
        print(end = '\n')
    print(end = '\n')
def main():
    floor = [[1, 0, 0, 0],
             [0, 1, 0, 1],
             [1, 0, 1, 1]]
    clean(floor)
main()
