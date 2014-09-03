import numpy as np

def gray_order(row1, row2, label=None):
    """
    input: two rows (numpy arrays) of adj matrix.
    lable: if there's a label in the first entry

    we assume no rows consist of all zeros

    """

    if label:
        row1 = row1[1]
        row2 = row2[1]
        i = np.nditer(np.nonzero(row1))
        j = np.nditer(np.nonzero(row2))
    else:
        i = np.nditer(np.nonzero(row1))
        j = np.nditer(np.nonzero(row2))

    p = False

    while True:

        try:
            a = i.next()
        except:
            a = np.inf
        try:
            b = j.next()
        except:
            b = np.inf

        if i.finished and j.finished:
            return 0

        if a != b:
            if p ^ (a < b):
                return 1
            else:
                return -1

        p = not p

# for a regular list of bits
order_unlabel = lambda a,b: gray_order(a, b, label=False)

# for the data (label in first entry)
order_label = lambda a,b: gray_order(a, b, label=True)

if __name__=="__main__":

    # these are ordered in lexicographic order
    a = np.array([0,0,1])
    b = np.array([0,1,0])
    c = np.array([0,1,1])
    d = np.array([1,0,0])
    e = np.array([1,0,1])
    f = np.array([1,1,0])
    g = np.array([1,1,1])

    # print their gray ordering
    print sorted([a,b,c,d,e,f,g], cmp=order_unlabel)
