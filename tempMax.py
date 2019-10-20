import matplotlib.pyplot as plt

meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
temperatura = ["31", "31", "31", "31", "30", "29", "29", "29", "29", "30", "31", "31"]

plt.title("temperaturas maximas registradas em recife (2018)")
plt.plot(meses, temperatura)
plt.ylim(100000, 120000)

plt.show()


