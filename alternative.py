import cmath

frequencia = 60  # Hz
omega = 2 * cmath.pi * frequencia  
def estrela_para_delta(za, zb, zc):
    z1 = (za * zb + zb * zc + zc * za) / zc
    z2 = (za * zb + zb * zc + zc * za) / za
    z3 = (za * zb + zb * zc + zc * za) / zb
    return z1, z2, z3

def calcular_capacitancia_indutancia(z, tipo):
    if tipo == 'indutancia':
        indutancia = z.imag / omega
        return indutancia  # Em Henrys
    elif tipo == 'capacitancia':
        capacitancia = -1 / (omega * z.imag)
        return capacitancia  # Em Farads
    return None

za = complex(60, -64.53)  # Impedância da fase A
zb = complex(60, -64.53)  # B
zc = complex(60, 0)       # C

z1, z2, z3 = estrela_para_delta(za, zb, zc)

print(f"Impedâncias na configuração delta:")
print(f"Z1 (entre fase A e B): {z1:.2f}")
print(f"Z2 (entre fase B e C): {z2:.2f}")
print(f"Z3 (entre fase C e A): {z3:.2f}")

for idx, z in enumerate([z1, z2, z3], start=1):
    if z.imag > 0:
        tipo = 'indutancia'
    elif z.imag < 0:
        tipo = 'capacitancia'
    else:
        tipo = 'resistência pura'

    if tipo == 'indutancia':
        valor = calcular_capacitancia_indutancia(z, 'indutancia')
        print(f"Z{idx} tem {valor:.6f} H de indutância")
    elif tipo == 'capacitancia':
        valor = calcular_capacitancia_indutancia(z, 'capacitancia')
        print(f"Z{idx} tem {valor:.6f} F de capacitância")
    else:
        print(f"Z{idx} é puramente resistivo, sem componente reativa.")
