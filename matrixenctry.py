import numpy as np



# A is Agreed Secret Key
# B is Msg in Numeric
# X is Encoded msg
# Ainv is inverse of Agreed Secret Key
# M is Decoded msg

# Getting the input from the user!
def Matrix_input():
    matrix = []

    rowno = int(input("Enter number of row:"))
    colno = int(input("Enter number of column:"))

    for i in range(rowno):
        row = []
        for j in range(colno):
            rw = int(input("Enter a element rowise " + str(i) + " " + str(j) + ":"))
            row.append(rw)

        matrix.append(row)

    print(matrix)

    M = np.array(matrix)
    print(M)
    print(type(M))

    return M


# Decoding
def Decoding(A):
    msg = []
    x = []

    print(A)
    A.round()
    print(A)

    X = A.shape
    Xrow = X[0]
    Xcol = X[1]
    print(Xrow)
    print(Xcol)

    for i in range(Xrow):
        for j in range(Xcol):
            print(round(A[i][j],1))
            round_A = round(A[i][j],1)
            x.append(int(round_A))

    print(x)

    Alpha = ['space','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'SPACE']

    for i in x:
        try:
            print("---------")
            print(i)
        except:
            print("index out of range")
        for j in range(28):
            if (i == j):
                print("matched")
                print(Alpha[j])
                msg.append(Alpha[j])



    print(msg)
    msg_arr = np.array(msg)
    msg = msg_arr.reshape(Xrow,Xcol)

    return msg


# Encrypting the msg from one side
def Encryption_team():
    print("Came to encryption part")

    print("Enter the agreed secret key:")
    A = Matrix_input()
    print(A)
    print("No of rows and colums" + str(A.shape))
    a = A.shape
    print(a[1])
    Acol = a[1]

    print("Enter the Numeric values for the Message from the table:")
    B = Matrix_input()
    print(B)
    print("No of rows and colums" + str(B.shape))
    b = B.shape
    Brow = b[0]

    # checking the condition for Multiplication
    # A no of colums = B no of Rows
    if (Acol == Brow):
        print("Dimension Matched")
        print("Encoded Msg be:")
        X = A.dot(B)
        print(X)
    else:
        print("Dimension Doesn't Match! Try to Correct the dimension")


# Decrypting the msg from other side
def Decryption_team():
    print("Came to Decryption Part")
    print("Enter the Agreed Secret Key:")
    A = Matrix_input()
    print(A)

    # Calculating the inverse of the matrix
    print("the inverse of secret key  Matrix is :")
    Ainv = np.linalg.inv(A)
    print(Ainv)
    print("After flooring!!")
    print(Ainv)
    ainv = Ainv.shape
    acol = ainv[1]

    # Encoded mag
    print("Enter the Encoded msg:")
    X = Matrix_input()
    print(X)
    x = X.shape
    xrow = x[0]

    # Decryption
    # checking the condition for Multiplication
    # A no of colums = B no of Rows
    if (acol == xrow):
        print("Dimension Matched")
        print("The Decoded Matrix in term of Matrix Format:")
        M = Ainv.dot(X)
        print(M)

        print("If we decode this we will get the msg!!")
        msgs = Decoding(M)
        print(msgs)
    else:
        print("Dimension Doesn't Match! Try to Correct the dimension")


def home():
    print("get the data from the user")
    print("Alpha-Numeric Value")
    Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'SPACE']
    i = 0
    while i < len(Alpha):
        print(Alpha[i] + "=" + str(i + 1), end='\t')
        i += 1

    print("\n1.Encryption \n2.Decryption")
    choice = int(input("Encryption or Decryption:"))
    if choice == 1:
        Encryption_team()
    else:
        Decryption_team()


home()


