from typing import List, Tuple


def palindrome_seq(seq: List[int], odd: bool):

    if odd:
        if len(seq) <= 1:
            raise IndexError('your seq is too short')
        palindrome = seq + list(reversed(seq))[1:]
    else:
        palindrome = seq + list(reversed(seq))

    return palindrome


def decode_continued_fraction(seq: List[int]):
    num, den = (0, 1), (1, 0)
    for u in reversed(seq):
        num, den = den, (den[0]*u + num[0], den[1]*u + num[1])
    return num, den


def get_equation(num: Tuple[int, int], dem: Tuple[int, int]):

    trace = (dem[0]-num[1], dem[1])
    norm = -num[0] / dem[1]

    return trace, norm


def main(seq:  List[int]):
    palindrome = palindrome_seq(seq, odd=True)
    print(palindrome)
    num, den = decode_continued_fraction(palindrome)
    trace, norm = get_equation(num, den)
    print('Norm', norm, ', so it is Galois extension')
    print('Trace', trace)


if __name__ == '__main__':
    main(seq=[1, 2, 3])
