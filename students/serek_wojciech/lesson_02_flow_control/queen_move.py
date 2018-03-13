#!/usr/bin/env python3
"""Queen move"""


def main():
    """Main function"""
    start_x = int(input())
    start_y = int(input())
    new_x = int(input())
    new_y = int(input())

    if abs(start_x - new_x) == abs(start_y - new_y) or \
       start_x == new_x or start_y == new_y:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
