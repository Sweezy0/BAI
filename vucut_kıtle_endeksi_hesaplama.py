print("Body Mass İndex Calculator")
height=float(input("height(m):"))
weight=int(input("weight(kg):"))
index=weight/(height*height)
if index<=18:
    print("\nweak BAI:{}".format(index))
elif index>18 and index<=25:
    print("\nweight BAI:{}".format(index))
elif index>25 and index<=30:
    print("\nobese BAI:{}".format(index))
