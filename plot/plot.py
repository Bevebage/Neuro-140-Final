import matplotlib.pyplot as plt

N = 7000

with open('log.txt') as f:
  data = f.readlines()
  wins = [row[row.index('won')+5: row.index('won')+6] for row in data]
  bars = [wins[i:i+100].count('T') for i in range(0, N, 100)]
  epsilon = [float(row[row.index('e:')+5: row.index('e:')+13]) for row in data]
  epsilonCum = [sum(epsilon[i:i+100])/100 for i in range(0, N, 100)]
  ax1 = plt.gca()
  ax2 = ax1.twinx()
  ax1.bar(list(range(N//100)), bars)

  ax1.set_xlabel('Games (100s)')
  ax1.set_ylabel('Number of games won (every 100)')

  ax2.plot(list(range(N//100)), epsilonCum, color='ORANGE')

  ax2.set_ylabel("Epsilon",rotation=-90,labelpad=15)
  plt.title('Performance and epsilon against number of games played')

  plt.savefig('new.png')
  plt.clf()