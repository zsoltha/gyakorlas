import random

print(f'''      Teszteld le a szerencsédet és a jövődet az új innovációs SZERENCSEGÉPEN''')
print('''               (Csak esélyen alapuló dolgokat kérdezhetsz)''')
em:int = input('Miben szeretnéd megtudni a szerencséd: ')
val = random.randint(0,10)

if val == 0 :
    print('Semmi eséllyel')
elif val < 3 :
    print('Hát a gép nem sok eséyt látt, hogy megfog történni')
elif val < 5:
    print('A gép azt mondja nem sok de van rá esély, hogy valóra válik')
elif val < 7 :
    print(f'Elég sok esély van, hogy meg fog történni de még mindig nem 100% ')
elif val < 9 :
    print('Nagyon sok rá az esély')
else:
    print(f'Szerecsés vagy mert az a dolog amit beírtál 100% hogy meg fog történni')
