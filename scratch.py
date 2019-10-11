with open("C:\\Users\\jsawd\\Desktop\\test\\eldfull.txt", "r") as my_collection:
    OWNED = my_collection.readlines()
    # collection read line per line
with open("C:\\Users\\jsawd\\Desktop\\test\\elddeck.txt", "r") as my_deck:
    DECK_LIST = my_deck.readlines()
    #decklist read lin for line

CUT_LIST = []
MISSING_LIST = []
NEED_LIST = []

for items in OWNED:
    cut_card = items.split(" (")

    cut2 = cut_card[0]
    cut2 = cut2[2:]
    CUT_LIST.append(cut2)




for each in DECK_LIST:
    card_raw = each.split(" (")
    card = card_raw[0]
    card = card[2:]
    NEED_LIST.append(card)
    if card not in CUT_LIST:
       MISSING_LIST.append(card)


print("you need: ")
for needed in NEED_LIST:
    print(needed)
#print("you have: ")
#for cut in CUT_LIST:
#    print(cut)
print(
      "/////////////////////////////////////////////"
      "////////////////////////////////////////////////"
      "///////////////////////////////////////////////////")
print("you're missing: ")
for missed in MISSING_LIST:
    print(missed)