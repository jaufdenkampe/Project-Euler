ranks = "23456789TJQKA"


def rank_hand(hand_list):
    straight = 0
    flush = 0
    hand_rank = []
    hand_rank.append(0)
    for x in range (0,len(hand_list)):
        top_card = hand_list[0]
        top_index = -1
        for y in range (0,len(hand_list)):
            if ranks.index(hand_list[y][0])>ranks.index(top_card[0]):
                top_card = hand_list[y]
                top_index = y
        hand_rank.append(top_card)
        
        hand_list.remove(top_card)
    
    
    flag = 0
    for x in range (1,5):
        for y in range (1,5):
            if x!=y and hand_rank[x][0]==hand_rank[y][0]:
                new_hand = []
                new_hand.append(1)
                new_hand.append(hand_rank[x])
                new_hand.append(hand_rank[y])
                hand_rank.remove(hand_rank[y])
                hand_rank.remove(hand_rank[x])
                hand_rank.remove(hand_rank[0])
                for card in hand_rank:
                    new_hand.append(card)
                hand_rank = new_hand
                flag = 1
                break
        if flag == 1:
            break
    new_hand = hand_rank
    if hand_rank[3][0]==hand_rank[4][0]:
        if ranks.index(hand_rank[1][0])>ranks.index(hand_rank[3][0]):
            new_hand = []
            new_hand.append(2)
            new_hand.append(hand_rank[1])
            new_hand.append(hand_rank[2])
            new_hand.append(hand_rank[3])
            new_hand.append(hand_rank[4])
            new_hand.append(hand_rank[5])
        else:
            new_hand = []
            new_hand.append(2)
            new_hand.append(hand_rank[3])
            new_hand.append(hand_rank[4])
            new_hand.append(hand_rank[1])
            new_hand.append(hand_rank[2])
            new_hand.append(hand_rank[5])
    if hand_rank[3][0]==hand_rank[5][0]:
        if ranks.index(hand_rank[1][0])>ranks.index(hand_rank[3][0]):
            new_hand = []
            new_hand.append(2)
            new_hand.append(hand_rank[1])
            new_hand.append(hand_rank[2])
            new_hand.append(hand_rank[3])
            new_hand.append(hand_rank[5])
            new_hand.append(hand_rank[4])
        else:
            new_hand = []
            new_hand.append(2)
            new_hand.append(hand_rank[3])
            new_hand.append(hand_rank[5])
            new_hand.append(hand_rank[1])
            new_hand.append(hand_rank[2])
            new_hand.append(hand_rank[5])
    if hand_rank[4][0]==hand_rank[5][0]:
        if ranks.index(hand_rank[1][0])>ranks.index(hand_rank[4][0]):
            new_hand = []
            new_hand.append(2)
            new_hand.append(hand_rank[1])
            new_hand.append(hand_rank[2])
            new_hand.append(hand_rank[4])
            new_hand.append(hand_rank[5])
            new_hand.append(hand_rank[3])
        else:
            new_hand = []
            new_hand.append(2)
            new_hand.append(hand_rank[4])
            new_hand.append(hand_rank[5])
            new_hand.append(hand_rank[1])
            new_hand.append(hand_rank[2])
            new_hand.append(hand_rank[3])
    hand_rank = new_hand

    

    if hand_rank[2][0]==hand_rank[3][0]:
        hand_rank[0]=3
        
    if hand_rank[2][0]==hand_rank[4][0]:
        new_hand = []
        new_hand.append(3)
        new_hand.append(hand_rank[1])
        new_hand.append(hand_rank[2])
        new_hand.append(hand_rank[4])
        new_hand.append(hand_rank[3])
        new_hand.append(hand_rank[5])
        hand_rank = new_hand
        
    if hand_rank[2][0]==hand_rank[5][0]:
        new_hand = []
        new_hand.append(3)
        new_hand.append(hand_rank[1])
        new_hand.append(hand_rank[2])
        new_hand.append(hand_rank[5])
        new_hand.append(hand_rank[3])
        new_hand.append(hand_rank[4])
        hand_rank = new_hand

    if hand_rank[3][0]==hand_rank[4][0] == hand_rank[5][0]:
        new_hand = []
        new_hand.append(3)
        new_hand.append(hand_rank[3])
        new_hand.append(hand_rank[4])
        new_hand.append(hand_rank[5])
        new_hand.append(hand_rank[1])
        new_hand.append(hand_rank[2])
        hand_rank = new_hand

    if ranks.index(hand_rank[2][0]) == ranks.index(hand_rank[1][0])-1:
        if ranks.index(hand_rank[3][0]) == ranks.index(hand_rank[1][0])-2:
            if ranks.index(hand_rank[4][0]) == ranks.index(hand_rank[1][0])-3:
                if ranks.index(hand_rank[5][0]) == ranks.index(hand_rank[1][0])-4:
                    hand_rank[0]=4
                    straight = 1

    if (hand_rank[1][0]) == "A":
        if (hand_rank[2][0]) == "5":
            if (hand_rank[3][0]) == "4":
                if (hand_rank[4][0]) == "3":
                    if (hand_rank[5][0]) == "2":
                        new_hand = []
                        new_hand.append(5)
                        new_hand.append(hand_rank[2])
                        new_hand.append(hand_rank[3])
                        new_hand.append(hand_rank[4])
                        new_hand.append(hand_rank[5])
                        new_hand.append(hand_rank[1])
                        hand_rank = new_hand
                        straight = 1

    if (hand_rank[2][1]) == (hand_rank[1][1]):
        if (hand_rank[3][1]) == (hand_rank[1][1]):
            if (hand_rank[4][1]) == (hand_rank[1][1]):
                if (hand_rank[5][1]) == (hand_rank[1][1]):
                    hand_rank[0]=5
                    flush = 1
                    
    if hand_rank[0] == 3 and hand_rank[4][0] == hand_rank[5][0]:
        hand_rank[0] = 6
        
    if hand_rank[0] == 3 and hand_rank[3][0] == hand_rank[4][0]:
        hand_rank[0] = 7
    
    if hand_rank[0] == 3 and hand_rank[3][0] == hand_rank[5][0]:
        hand_rank[0] = 7
    
    if flush == 1 and straight == 1:
        hand_rank[0] = 8
        
    if hand_rank[0] == 8 and hand_rank[1][0] == 'A':
        hand_rank[0] = 9
    

    
    return (hand_rank)
        
        



hands = open("pokerhands.txt").readlines()
print (hands)
print (hands[0])
hand = hands[0]
plyr1hand = []
plyr2hand = []
plyr1_wins = 0
print (len(hands))
for y in range(0,1000):
    hand = hands[y]
    plyr1hand = []
    plyr2hand = []
    for x in range (0,5):
        card = []
        card.append(hand[3*x])
        card.append(hand[3*x+1])
        plyr1hand.append(card)
        card = []
        card.append(hand[15+3*x])
        card.append(hand[+15+3*x+1])
        plyr2hand.append(card)

    print (plyr1hand)
    print (plyr2hand)
    plyr1score = rank_hand(plyr1hand)
    plyr2score = rank_hand(plyr2hand)
    if plyr1score[0]>plyr2score[0]:
        plyr1_wins = plyr1_wins+1


    if plyr1score[0]==plyr2score[0] and ranks.index(plyr1score[1][0])>ranks.index(plyr2score[1][0]):
        plyr1_wins = plyr1_wins+1


    if plyr1score[0]==plyr2score[0] and ranks.index(plyr1score[1][0])==ranks.index(plyr2score[1][0]):
        if ranks.index(plyr1score[2][0])>ranks.index(plyr2score[2][0]):
            plyr1_wins = plyr1_wins+1
            
    if plyr1score[0]==plyr2score[0] and ranks.index(plyr1score[1][0])==ranks.index(plyr2score[1][0]):
        if ranks.index(plyr1score[2][0])==ranks.index(plyr2score[2][0]):
            if ranks.index(plyr1score[3][0])>ranks.index(plyr2score[3][0]):
                plyr1_wins = plyr1_wins+1
            
    if plyr1score[0]==plyr2score[0] and ranks.index(plyr1score[1][0])==ranks.index(plyr2score[1][0]):
        if ranks.index(plyr1score[2][0])==ranks.index(plyr2score[2][0]):
            if ranks.index(plyr1score[3][0])==ranks.index(plyr2score[3][0]):
                if ranks.index(plyr1score[4][0])>ranks.index(plyr2score[4][0]):
                    plyr1_wins = plyr1_wins+1
            
    if plyr1score[0]==plyr2score[0] and ranks.index(plyr1score[1][0])==ranks.index(plyr2score[1][0]):
        if ranks.index(plyr1score[2][0])==ranks.index(plyr2score[2][0]):
            if ranks.index(plyr1score[3][0])==ranks.index(plyr2score[3][0]):
                if ranks.index(plyr1score[4][0])==ranks.index(plyr2score[4][0]):
                    if ranks.index(plyr1score[5][0])>=ranks.index(plyr2score[5][0]):
            
                        plyr1_wins = plyr1_wins+1
                        
print (plyr1_wins)

print (rank_hand([['9','S'],['Q', 'S'], ['T', 'S'], ['J', 'S'], ['K', 'S']]))