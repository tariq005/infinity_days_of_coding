for i in range(int(input())):
    p, a, b, c= map(int, input().split())

    if p%a == 0 or p%b == 0 or p%c == 0:
        print(0)
    else:
        print(min(a-(p%a), b-(p%b), c-(p%c)))