#!/usr/bin/python3
'''A script that can determine the pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of items of integers representing the Pascal’s triangle
    '''
    items = []
    if n == 0:
        return items
    for i in range(n):
        items.append([])
        items[i].append(1)
        if (i > 0):
            for j in range(1, i):
                items[i].append(items[i - 1][j - 1] + items[i - 1][j])
            items[i].append(1)
    return items
