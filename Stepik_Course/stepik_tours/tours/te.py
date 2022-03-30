from data import tours

tour_id = {}

for i, y in tours.items():
    if y["departure"] == 'msk':
        tour_id[i] = y

sums = []
night = []
for i, y in tour_id.items():
    sums.append(y["price"])
    night.append(y["nights"])

print(sums)
print(night)
