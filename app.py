from flask import Flask, render_template, request

app = Flask(__name__)

# Data Produk (Simulasi data)
PRODUCTS = [
    {"nama": "Sistem Kasir Cloud", "desc": "Aplikasi manajemen stok dan penjualan real-time.", "harga": "Rp 500.000"},
    {"nama": "Jasa SEO Digital", "desc": "Optimasi website agar muncul di halaman utama pencarian.", "harga": "Rp 1.200.000"},
    {"nama": "Desain UI/UX", "desc": "Pembuatan prototipe aplikasi mobile yang user-friendly.", "harga": "Rp 850.000"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/produk')
def produk():
    return render_template('produk.html', produk_list=PRODUCTS)

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    if request.method == 'POST':
        nama = request.form.get('nama')
        email = request.form.get('email')
        pesan = request.form.get('pesan')
        return render_template('response.html', nama=nama, email=email, pesan=pesan)
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)
