import matplotlib.pyplot as plt
import numpy as np

equilibrium = 1
x0 = 1.3
v0 = 0
m = 1
k = 1e4
dt = 1e-5
t = 0.1
x_list = []
v_list = []
t_list = []
E_list = []
Ek_list = []
Ep_list = []

def acceleration(x):
    dx = x - equilibrium
    a = - (k / m) * dx
    return a

def euler(x0, v0):
    x_old = x0
    v_old = v0
    for time in np.arange(0, t, dt):
        a = acceleration(x_old)
        v_new = v_old + a * dt
        x_new = x_old + v_old * dt

        energy = calc_energy(x_new, v_new)

        x_list.append(x_new)
        v_list.append(v_new)
        t_list.append(time)
        E_list.append(energy[2])
        Ek_list.append(energy[1])
        Ep_list.append(energy[0])

        x_old = x_new
        v_old = v_new

    return x_list, v_list, t_list, E_list, Ek_list, Ep_list

def verlet(x0, v0):
    for time in np.arange(0, t, dt):
        a = acceleration(x0)
        x = x0 + v0 * dt + 1/2 * a * dt ** 2
        a2 = acceleration(x)
        v = v0 + 1/2 * (a + a2) * dt

        energy = calc_energy(x, v)

        x_list.append(x)
        v_list.append(v)
        t_list.append(time)
        E_list.append(energy[2])
        Ek_list.append(energy[1])
        Ep_list.append(energy[0])

        x0 = x
        v0 = v

    return x_list, v_list, t_list, E_list, Ek_list, Ep_list

def calc_energy(x, v):
    Ep = 0.5 * k * x ** 2
    Ek = 0.5 * m * v ** 2
    E = Ep + Ek
    # print(E, Ep, Ek)
    return Ep, Ek, E

def plotting(x0, v0):
    t_list = euler(x0, v0)[2]
    eul = euler(x0, v0)
    ver = verlet(x0, v0)

    x_eul = eul[0]
    v_eul = eul[1]
    E_eul = eul[3]
    Ek_eul = eul[4]
    Ep_eul = eul[5]

    v_ver = ver[1]
    x_ver = ver[0]
    E_ver = ver[3]
    Ek_ver = ver[4]
    Ep_ver = ver[5]

    # plt.plot(t_list, E_ver, 'g-', label='verlet')
    plt.plot(t_list, x_eul, '--r', label='eul')
    # plt.plot(t_list, Ek_eul, 'g-', label='eul')
    plt.xlabel("t")
    plt.ylabel("x")
    plt.show()
    
    # for i in range(len(t_list)):
    #     print t_list[i], x_eul[i]

plotting(x0, v0)
