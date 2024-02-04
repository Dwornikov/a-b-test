import scipy.stats as stats

# Заданные значения
alpha = 0.05
beta = 0.20
sd = 156
delta = 0.10  
mean_daily_traffic = 20000
mean_time_spent = 25  

# Находим Z-значения 
z_alpha_half = stats.norm.ppf(1 - alpha / 2)
z_beta = stats.norm.ppf(1 - beta)

# Рассчитываем размер выборки
n = ((z_alpha_half + z_beta) ** 2 * sd ** 2) / (delta ** 2 * mean_time_spent ** 2)

# Рассчитываем длительность эксперимента в днях
experiment_duration = n / mean_daily_traffic

print(f"Размер выборки: {round(n)}")
print(f"Длительность эксперимента (в днях): {round(experiment_duration)}")
