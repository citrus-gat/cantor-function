'''
Plotting f_n for the sequence of functions that defines the Cantor function using matplotlib 
'''

import argparse
import matplotlib.pyplot as plt
# import numpy as np 

# If (x0, y0) to (xt, yt) is slopy, create a staircase 
# and return those 4 points 
def createStairCase(x0, y0, xt, yt):
    delta_x = (xt - x0)/3
    x1 = delta_x + x0
    x2 = delta_x + x1
    delta_y = (yt - y0)/2
    y = y0 + delta_y
    return [[x0, y0], [x1, y], [x2, y], [xt, yt]]


# Assume len(dots) is even 
# Structure: [[x0, y0], [x1, y1], ..., [xn, yn]]
def iterate(dots):
    newdots = []
    for i in range(len(dots)//2):
        pt1, pt2 = dots[2*i], dots[2*i+1]
        if pt2[1] == pt1[1]:
            newdots.append(pt1)
            newdots.append(pt2)
        else:
            newdots.extend(createStairCase(*pt1, *pt2))
    return newdots

# Compute the nth function in the sequence 
def fn(n):
    dots = [[0,0],[1,1]]
    for _ in range(n):
        dots = iterate(dots)
    return dots

# from [[x0, y0], [x1, y1], ..., [xn, yn]] to ([x0, x1, ...], [y0, y1, ...])
def transpose(dots):
    xs = [pt[0] for pt in dots]
    ys = [pt[1] for pt in dots]
    return xs, ys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--n", dest='n', type=int, default=10,
                        help="n-th iteration in the construction of the cantor function")
    parser.add_argument("-m", "--measure", action="store_true",
                        help="Output the measure (or length) of the regions where the function is increasing")
    args = parser.parse_args()

    n = args.n 

    print('Generating function...')
    dots = fn(n)
    
    xs, ys = transpose(dots)

    # Approximate the measure of C_n, which is where the function is increasing 
    if args.measure: 
        # Notice that the increasing region is the union of disjoint intervals, 
        # so it is measureable, and the measure is the sum of the "length" or "volume"
        # of the intervals, which is right endpoint - left endpoint
        m = 0
        for i in range(len(xs)-1): 
            if ys[i+1] != ys[i]:
                m += (xs[i+1] - xs[i])
        print('measure (length) of the increasing region:', m)

    print('start plotting...')
    ftitle = r'$f_{' + str(n) + '}$'
    plt.plot(xs, ys)
    # plt.plot(xs, ys, 'go')
    # nextdots = iterate(dots)
    # next_xs, next_ys = transpose(nextdots)
    # plt.plot(next_xs, next_ys, 'go')
    # plt.plot([0,1],[0,1], 'go')
    # plt.text(0,0, '(0,0)')
    # plt.text(1,1, '(1,1)')
    # plt.plot([1/3,2/3,1/9,2/9,2/3+1/9,2/3+2/9],[1/2,1/2,1/4,1/4,3/4,3/4], 'go')
    # plt.text(1/9-0.01, 1/4+0.01, r'$\left(\dfrac{1}{9}, \dfrac{1}{4}\right)$', va='bottom', ha='center')
    # plt.text(2/9+0.01, 1/4+0.01, r'$\left(\dfrac{2}{9}, \dfrac{1}{4}\right)$', va='bottom', ha='center')
    # plt.text(7/9-0.01, 3/4+0.01, r'$\left(\dfrac{7}{9}, \dfrac{3}{4}\right)$', va='bottom', ha='center')
    # plt.text(8/9+0.01, 3/4+0.01, r'$\left(\dfrac{8}{9}, \dfrac{3}{4}\right)$', va='bottom', ha='center')
    # plt.xticks(xs)
    # plt.yticks(ys)
    # print(xs)
    plt.title(ftitle)
    plt.show()

if __name__ == '__main__':
    main()
