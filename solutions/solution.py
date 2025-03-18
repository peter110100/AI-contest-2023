def solution(N):
    binary = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    for digit in binary:
        if digit == '1':
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        else:
            current_gap += 1
    return max_gap