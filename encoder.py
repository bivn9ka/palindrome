from typing import List


def palindromed_seq(seq: List):

    palindromed_seq = seq + list(reversed(seq))

    return palindromed_seq


def get_continued_fracted(seq):
    num, den = (0, 1), (1, 0)
    for u in reversed(seq):
        num, den = den, (den[0]*u + num[0], den[1]*u + num[1])
    return num, den


def get_equation(num, dem):

    trace = (dem[0]-num[1], dem[1])
    norm = -num[0] / dem[1]

    return trace, norm

def main():
    # Get the the number of terms, less one
    seq = [1, 2, 3]
    palindrome = palindromed_seq(seq)
    num, den = get_continued_fracted(palindrome)
    trace, norm = get_equation(num, den)
    print('Norm', norm, ', so it is Galois extension')
    print('Trace', trace, norm)

if __name__ == '__main__':
    main()