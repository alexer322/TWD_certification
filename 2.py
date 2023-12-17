# pull_ups
# 	x	6-8 	9-11 	12-14	15-17	18+
# 	x	м	ж	м	ж	м	ж	м	ж	м	ж
# l1	5	5	0	6	0	9	0	11	0	13	0
# l2	4	3	0	4	0	6	0	7	0	9	0
# l3	3	1	0	2	0	3	0	4	0	6	0
# l4	2	0	0	1	0	1	0	1	0	2	0



# вычитываем файл в листы по упражнениям
# определяем возраст и пол

f = open('C:\workdir\TWD_certification\check_data\8gp.txt', 'r')


l = [line.split("	") for line in f]
print(l[0])
l2=(l[1])

# print(l)
print(l2)



f.close()