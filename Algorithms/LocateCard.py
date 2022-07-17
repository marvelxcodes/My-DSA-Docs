def LocateCard(cards: list[int], query:int):
    position = -1
    for i in range(0, len(cards)):
        if cards[i] == query:
            position = i
            break
    return position
