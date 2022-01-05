def solution(lottos, win_nums):
    answer = []
    rank = 7
    zero = 0

    for i in lottos:
        rank -= win_nums.count(i)
    zero = lottos.count(0)

    if rank > 6:
        rank = 6
    if zero == 6:
        zero -= 1
    answer.append(rank - zero)
    answer.append(rank)
    return answer