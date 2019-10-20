import matplotlib.pyplot as plt

data = {"jan": 31, "fev": 31, "mar": 31, "abr": 31, "mai": 30, "jun": 29, "jul": 29, "ago": 29, "set": 29, "out": 30, "nov": 31, "dez": 31}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
#axs[1].scatter(names, values)
#axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

plt.show()

