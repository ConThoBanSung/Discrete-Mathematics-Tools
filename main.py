import tkinter as tk
from tkinter import messagebox
import math
import statistics

class DiscreteMathTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Công cụ Toán Rời Rạc")

        # Khởi tạo các frame
        self.init_comb_perm_frame()
        self.init_binomial_frame()
        self.init_probability_frame()
        self.init_graph_theory_frame()
        self.init_fibonacci_frame()
        self.init_additional_frame()
        self.init_statistics_frame()
        self.init_set_operations_frame()
        self.init_gcd_lcm_frame()

    def init_comb_perm_frame(self):
        frame = tk.LabelFrame(self.root, text="Tổ hợp và Hoán vị")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.entry_n = self.create_label_entry(frame, "Nhập n:", 0)
        self.entry_k = self.create_label_entry(frame, "Nhập k:", 1)

        tk.Button(frame, text="Tính Tổ hợp", command=self.calculate_combination).grid(row=2, column=0)
        tk.Button(frame, text="Tính Hoán vị", command=self.calculate_permutation).grid(row=2, column=1)
        tk.Button(frame, text="Tổ hợp với lặp lại", command=self.calculate_combination_with_replacement).grid(row=3, column=0)
        tk.Button(frame, text="Hoán vị với lặp lại", command=self.calculate_permutation_with_replacement).grid(row=3, column=1)

    def init_binomial_frame(self):
        frame = tk.LabelFrame(self.root, text="Định lý nhị thức Newton")
        frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.entry_a = self.create_label_entry(frame, "Nhập a:", 0)
        self.entry_b = self.create_label_entry(frame, "Nhập b:", 1)
        self.entry_n_binom = self.create_label_entry(frame, "Nhập n:", 2)

        tk.Button(frame, text="Tính nhị thức", command=self.calculate_binomial).grid(row=3, column=0, columnspan=2)

    def init_probability_frame(self):
        frame = tk.LabelFrame(self.root, text="Xác suất")
        frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.entry_event = self.create_label_entry(frame, "Số phần tử biến cố:", 0)
        self.entry_sample = self.create_label_entry(frame, "Số phần tử không gian mẫu:", 1)

        tk.Button(frame, text="Tính Xác suất", command=self.calculate_probability).grid(row=2, column=0, columnspan=2)
        tk.Button(frame, text="Xác suất điều kiện", command=self.calculate_conditional_probability).grid(row=3, column=0, columnspan=2)

    def init_graph_theory_frame(self):
        frame = tk.LabelFrame(self.root, text="Lý thuyết đồ thị")
        frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        self.entry_edges = self.create_label_entry(frame, "Số cạnh:", 0)

        tk.Button(frame, text="Tính bậc đỉnh", command=self.calculate_handshake).grid(row=1, column=0, columnspan=2)

    def init_fibonacci_frame(self):
        frame = tk.LabelFrame(self.root, text="Dãy Fibonacci")
        frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        self.entry_fib = self.create_label_entry(frame, "Nhập n:", 0)

        tk.Button(frame, text="Tính dãy Fibonacci", command=self.calculate_fibonacci).grid(row=1, column=0, columnspan=2)

    def init_additional_frame(self):
        frame = tk.LabelFrame(self.root, text="Phép tính bổ sung")
        frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        self.entry_set_size = self.create_label_entry(frame, "Kích thước tập hợp (n):", 0)
        self.entry_arrangement = self.create_label_entry(frame, "Số phần tử (k):", 1)

        tk.Button(frame, text="Tính sắp xếp", command=self.calculate_arrangements).grid(row=2, column=0)
        tk.Button(frame, text="Tính tổ hợp", command=self.calculate_combination).grid(row=2, column=1)

    def init_statistics_frame(self):
        frame = tk.LabelFrame(self.root, text="Thống kê")
        frame.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

        self.entry_numbers = self.create_label_entry(frame, "Nhập các số cách nhau bởi dấu phẩy:", 0)

        tk.Button(frame, text="Tính Giá trị Trung bình", command=self.calculate_mean).grid(row=1, column=0)
        tk.Button(frame, text="Tính Phương sai", command=self.calculate_variance).grid(row=1, column=1)
        tk.Button(frame, text="Tính Độ lệch chuẩn", command=self.calculate_stddev).grid(row=2, column=0)
        tk.Button(frame, text="Kiểm tra tính chẵn lẻ", command=self.check_even_odd).grid(row=2, column=1)
        tk.Button(frame, text="Tính tổng chuỗi số", command=self.calculate_sum).grid(row=3, column=0)
        tk.Button(frame, text="Tính tích chuỗi số", command=self.calculate_product).grid(row=3, column=1)

    def init_set_operations_frame(self):
        frame = tk.LabelFrame(self.root, text="Phép toán trên tập hợp")
        frame.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

        self.entry_set_a = self.create_label_entry(frame, "Nhập tập A (cách nhau bởi dấu phẩy):", 0)
        self.entry_set_b = self.create_label_entry(frame, "Nhập tập B (cách nhau bởi dấu phẩy):", 1)

        tk.Button(frame, text="Tính hợp", command=self.calculate_union).grid(row=2, column=0)
        tk.Button(frame, text="Tính giao", command=self.calculate_intersection).grid(row=2, column=1)
        tk.Button(frame, text="Tính hiệu", command=self.calculate_difference).grid(row=3, column=0)
        tk.Button(frame, text="Tính bù", command=self.calculate_complement).grid(row=3, column=1)

    def init_gcd_lcm_frame(self):
        frame = tk.LabelFrame(self.root, text="GCD và LCM")
        frame.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')

        self.entry_gcd_lcm = self.create_label_entry(frame, "Nhập các số cách nhau bởi dấu phẩy:", 0)

        tk.Button(frame, text="Tính GCD", command=self.calculate_gcd).grid(row=1, column=0)
        tk.Button(frame, text="Tính LCM", command=self.calculate_lcm).grid(row=1, column=1)

    def create_label_entry(self, parent, label_text, row):
        tk.Label(parent, text=label_text).grid(row=row, column=0)
        entry = tk.Entry(parent)
        entry.grid(row=row, column=1)
        return entry

    def get_entry_value(self, entry):
        try:
            return int(entry.get())
        except ValueError:
            return "Không hợp lệ"

    def get_numbers_from_entry(self, entry):
        try:
            return list(map(float, entry.get().split(',')))
        except ValueError:
            return "Không hợp lệ"

    def combination(self, n, k):
        try:
            return math.comb(n, k)
        except ValueError:
            return "Không hợp lệ"

    def permutation(self, n, k):
        try:
            return math.perm(n, k)
        except ValueError:
            return "Không hợp lệ"

    def combination_with_replacement(self, n, k):
        try:
            return math.comb(n + k - 1, k)
        except ValueError:
            return "Không hợp lệ"

    def permutation_with_replacement(self, n, k):
        return n ** k

    def binomial_theorem(self, a, b, n):
        result = []
        for k in range(n + 1):
            term = self.combination(n, k) * (a ** (n - k)) * (b ** k)
            result.append(str(term))
        return " + ".join(result)

    def probability(self, event_size, sample_size):
        try:
            return event_size / sample_size
        except ZeroDivisionError:
            return "Không hợp lệ"

    def conditional_probability(self, event_size, given_event_size):
        try:
            return event_size / given_event_size
        except ZeroDivisionError:
            return "Không hợp lệ"

    def calculate_combination(self):
        n = self.get_entry_value(self.entry_n)
        k = self.get_entry_value(self.entry_k)
        result = self.combination(n, k)
        messagebox.showinfo("Kết quả Tổ hợp", f"C({n}, {k}) = {result}")

    def calculate_permutation(self):
        n = self.get_entry_value(self.entry_n)
        k = self.get_entry_value(self.entry_k)
        result = self.permutation(n, k)
        messagebox.showinfo("Kết quả Hoán vị", f"P({n}, {k}) = {result}")

    def calculate_combination_with_replacement(self):
        n = self.get_entry_value(self.entry_n)
        k = self.get_entry_value(self.entry_k)
        result = self.combination_with_replacement(n, k)
        messagebox.showinfo("Kết quả Tổ hợp với lặp lại", f"C({n}, {k}) = {result}")

    def calculate_permutation_with_replacement(self):
        n = self.get_entry_value(self.entry_n)
        k = self.get_entry_value(self.entry_k)
        result = self.permutation_with_replacement(n, k)
        messagebox.showinfo("Kết quả Hoán vị với lặp lại", f"P({n}, {k}) = {result}")

    def calculate_binomial(self):
        a = self.get_entry_value(self.entry_a)
        b = self.get_entry_value(self.entry_b)
        n = self.get_entry_value(self.entry_n_binom)
        result = self.binomial_theorem(a, b, n)
        messagebox.showinfo("Kết quả Định lý nhị thức", f"({a} + {b})^{n} = {result}")

    def calculate_probability(self):
        event_size = self.get_entry_value(self.entry_event)
        sample_size = self.get_entry_value(self.entry_sample)
        result = self.probability(event_size, sample_size)
        messagebox.showinfo("Kết quả Xác suất", f"P = {result}")

    def calculate_conditional_probability(self):
        event_size = self.get_entry_value(self.entry_event)
        given_event_size = self.get_entry_value(self.entry_sample)  # Assuming the second entry is given event size
        result = self.conditional_probability(event_size, given_event_size)
        messagebox.showinfo("Kết quả Xác suất điều kiện", f"P(A|B) = {result}")

    def calculate_handshake(self):
        edges = self.get_entry_value(self.entry_edges)
        if edges == "Không hợp lệ":
            return
        # Calculate degree of vertex
        degree = edges * 2
        messagebox.showinfo("Kết quả", f"Bậc đỉnh = {degree}")

    def calculate_fibonacci(self):
        n = self.get_entry_value(self.entry_fib)
        if n < 0:
            messagebox.showinfo("Kết quả", "Không có số Fibonacci cho n âm.")
            return

        a, b = 0, 1
        fib_sequence = []
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b

        messagebox.showinfo("Kết quả Dãy Fibonacci", f"Dãy Fibonacci: {fib_sequence}")

    def calculate_arrangements(self):
        n = self.get_entry_value(self.entry_set_size)
        k = self.get_entry_value(self.entry_arrangement)
        arrangements = self.permutation(n, k)
        messagebox.showinfo("Kết quả Sắp xếp", f"Sắp xếp {k} trong {n} = {arrangements}")

    def calculate_mean(self):
        numbers = self.get_numbers_from_entry(self.entry_numbers)
        if numbers == "Không hợp lệ":
            return
        mean = statistics.mean(numbers)
        messagebox.showinfo("Kết quả", f"Giá trị trung bình: {mean}")

    def calculate_variance(self):
        numbers = self.get_numbers_from_entry(self.entry_numbers)
        if numbers == "Không hợp lệ":
            return
        variance = statistics.variance(numbers)
        messagebox.showinfo("Kết quả", f"Phương sai: {variance}")

    def calculate_stddev(self):
        numbers = self.get_numbers_from_entry(self.entry_numbers)
        if numbers == "Không hợp lệ":
            return
        stddev = statistics.stdev(numbers)
        messagebox.showinfo("Kết quả", f"Độ lệch chuẩn: {stddev}")

    def check_even_odd(self):
        numbers = self.get_numbers_from_entry(self.entry_numbers)
        if numbers == "Không hợp lệ":
            return
        results = ["Chẵn" if num % 2 == 0 else "Lẻ" for num in numbers]
        messagebox.showinfo("Kết quả", f"Chẵn/Lẻ: {results}")

    def calculate_sum(self):
        numbers = self.get_numbers_from_entry(self.entry_numbers)
        if numbers == "Không hợp lệ":
            return
        total_sum = sum(numbers)
        messagebox.showinfo("Kết quả", f"Tổng: {total_sum}")

    def calculate_product(self):
        numbers = self.get_numbers_from_entry(self.entry_numbers)
        if numbers == "Không hợp lệ":
            return
        product = math.prod(numbers)
        messagebox.showinfo("Kết quả", f"Tích: {product}")

    def calculate_union(self):
        set_a = set(self.get_numbers_from_entry(self.entry_set_a))
        set_b = set(self.get_numbers_from_entry(self.entry_set_b))
        union_result = set_a.union(set_b)
        messagebox.showinfo("Kết quả Hợp", f"Hợp của A và B: {union_result}")

    def calculate_intersection(self):
        set_a = set(self.get_numbers_from_entry(self.entry_set_a))
        set_b = set(self.get_numbers_from_entry(self.entry_set_b))
        intersection_result = set_a.intersection(set_b)
        messagebox.showinfo("Kết quả Giao", f"Giao của A và B: {intersection_result}")

    def calculate_difference(self):
        set_a = set(self.get_numbers_from_entry(self.entry_set_a))
        set_b = set(self.get_numbers_from_entry(self.entry_set_b))
        difference_result = set_a.difference(set_b)
        messagebox.showinfo("Kết quả Hiệu", f"Hiệu của A và B: {difference_result}")

    def calculate_complement(self):
        set_a = set(self.get_numbers_from_entry(self.entry_set_a))
        set_b = set(self.get_numbers_from_entry(self.entry_set_b))
        complement_result = set_b.difference(set_a)
        messagebox.showinfo("Kết quả Bù", f"Bù của A trong B: {complement_result}")

    def calculate_gcd(self):
        numbers = self.get_numbers_from_entry(self.entry_gcd_lcm)
        if numbers == "Không hợp lệ":
            return
        gcd_result = math.gcd(*map(int, numbers))
        messagebox.showinfo("Kết quả GCD", f"GCD: {gcd_result}")

    def calculate_lcm(self):
        numbers = self.get_numbers_from_entry(self.entry_gcd_lcm)
        if isinstance(numbers, str):
            messagebox.showerror("Lỗi", "Vui lòng nhập các số hợp lệ, cách nhau bởi dấu phẩy.")
            return

        if len(numbers) < 2:
            messagebox.showerror("Lỗi", "Cần ít nhất hai số để tính LCM.")
            return

    # Chuyển đổi tất cả các số sang kiểu int
        numbers = [int(num) for num in numbers]

        lcm_result = abs(numbers[0] * numbers[1]) // math.gcd(numbers[0], numbers[1])
        for num in numbers[2:]:
            lcm_result = abs(lcm_result * num) // math.gcd(lcm_result, num)

        messagebox.showinfo("Kết quả", f"LCM của {numbers} là {lcm_result}.")



if __name__ == "__main__":
    root = tk.Tk()
    app = DiscreteMathTool(root)
    root.mainloop()
