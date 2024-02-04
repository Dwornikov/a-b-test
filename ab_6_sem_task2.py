import scipy.stats as stats


alpha = 0.05
beta = 0.20
mean_daily_traffic = 4000

# Находим Z-значения 
z_alpha_half = stats.norm.ppf(1 - alpha / 2)
z_beta = stats.norm.ppf(1 - beta)

# Текущая и ожидаемая конверсии, минимально значимый эффект
p1 = 0.40 
p2 = 0.40 * 0.8 
delta = p1 - p2  

# Рассчитываем размер выборки
n = ((z_alpha_half + z_beta) ** 2 * p1 * (1 - p1) + p2 * (1 - p2)) / delta**2

# Рассчитываем длительность эксперимента в днях
experiment_duration = n / mean_daily_traffic

print(f"Размер выборки: {round(n)}")
print(f"Длительность эксперимента (в днях): {round(experiment_duration)}")
