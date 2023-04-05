class Employee:

    def __init__(self, name, salary, grade, num_children, married):

        self.name = name

        self.salary = salary

        self.grade = grade

        self.num_children = num_children

        self.married = married

    def get_salary(self):

        # Hitung tunjangan golongan

        if self.grade == 1:

            allowance_grade = 0.05 * self.salary

        elif self.grade == 2:

            allowance_grade = 0.1 * self.salary

        elif self.grade == 3:

            allowance_grade = 0.15 * self.salary

        elif self.grade == 4:

            allowance_grade = 0.2 * self.salary

        elif self.grade == 5:

            allowance_grade = 0.25 * self.salary

        # Hitung tunjangan anak

        if self.num_children > 0:

            allowance_children = 0.02 * self.salary * self.num_children

        else:

            allowance_children = 0    

        # Hitung tunjangan istri

        if self.married:

            allowance_spouse = 0.1 * self.salary

        else:

            allowance_spouse = 0       

        # Hitung total gaji sebelum pajak

        total_salary = self.salary + allowance_grade + allowance_children + allowance_spouse  

        # Hitung pajak

        if total_salary <= 5000000:

            tax = 0.05 * total_salary

        elif total_salary <= 10000000:

            tax = 0.1 * total_salary

        else:

            tax = 0.15 * total_salary    

        # Hitung bonus

        if self.grade == 3 and self.num_children >= 3:

            bonus = 500000

        elif self.grade == 4:

            bonus = 750000

        elif self.grade == 5:

            bonus = 1000000

        else:

            bonus = 0

        # Hitung total gaji setelah pajak dan bonus

        total_salary = total_salary - tax + bonus

        return total_salary

# Meminta input dari pengguna
name = input("Masukkan nama karyawan: ")
salary = int(input("Masukkan gaji pokok: "))
grade = int(input("Masukkan golongan (1-5): "))
num_children = int(input("Masukkan jumlah anak: "))
married = input("Apakah karyawan sudah menikah? (y/n): ")

if married == "y":
    married = True
else:
    married = False

# Membuat objek karyawan dengan input pengguna
employee = Employee(name, salary, grade, num_children, married)

# Menampilkan gaji karyawan setelah diproses
print("Gaji karyawan ", employee.name, " adalah: Rp ", employee.get_salary())
