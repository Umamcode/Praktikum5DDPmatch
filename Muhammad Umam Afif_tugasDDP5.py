{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOeQP0phAmlvfIwxWD1fnqf"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":17,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"24W1KfFSg0gN","executionInfo":{"status":"ok","timestamp":1698135008129,"user_tz":-420,"elapsed":1364,"user":{"displayName":"Muhammad Umam Afif","userId":"00412766930112587672"}},"outputId":"edfaca6c-f8e4-4591-f736-b221c708a414"},"outputs":[{"output_type":"stream","name":"stdout","text":["['BG1803', 'Civic', 'Honda', 'Mobil', '2000cc', 'Merah', 'Rp.600jt', 'roda empat']\n"]}],"source":["# No1\n","Kendaraan = [\"BG1803\", \"Civic\", \"2000cc\", \"Merah\"]\n","# No2\n","Kendaraan.append(\"Rp.600jt\")\n","Kendaraan.append(\"roda empat\")\n","Kendaraan.insert(2,\"Honda\")\n","Kendaraan.insert(3,\"Mobil\")\n","print(Kendaraan)"]},{"cell_type":"code","source":["\n","pesan = \"\"\"\n","Mau mengitung apa?\n","Pilihan :\n","1. Menghitung Luas Persegi\n","2. Meghitung Luas Lingkaran\n","3. Menghitung Luas Segitiga\n","\"\"\"\n","pilihan = input (pesan)\n","\n","match pilihan:\n","   case \"1\":\n","       print(\"Menghitung Luas Persegi\")\n","       print(\"Rumus = sisi x sisi\")\n","       sisi = int(input (\"masukan sisi :\"))\n","       luasp = sisi * sisi\n","       print(\"Luas Perseginya adalah :\", luasp)\n","   case \"2\":\n","       print(\"Menghitung Luas Lingkaran\")\n","       print(\"Rumus = 3,14 x r x r\")\n","       r = int(input (\"masukan jari-jari :\"))\n","       luasl = 3.14 * r * r\n","       print(\"Luas Lingkarannya adalah :\", luasl)\n","   case \"3\":\n","       print(\"Menghitung Luas Segitiga\")\n","       print(\"Rumus = 0.5 x alas x tinggi\")\n","       alas = int(input (\"masukan alas :\"))\n","       tinggi = int(input (\"masukan tinggi :\"))\n","       luass = 0.5 * alas * tinggi\n","       print(\"Luas Segitiganya adalah :\", luass)\n","   case _:\n","       print(\"salah memasukan pilihan\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Zpu4Ugu1jgPB","executionInfo":{"status":"ok","timestamp":1698134371318,"user_tz":-420,"elapsed":10998,"user":{"displayName":"Muhammad Umam Afif","userId":"00412766930112587672"}},"outputId":"ba8c1e7c-0835-4fdc-ba17-fdc19b9eb3fa"},"execution_count":16,"outputs":[{"output_type":"stream","name":"stdout","text":["\n","Mau mengitung apa?\n","Pilihan :\n","1. Menghitung Luas Persegi\n","2. Meghitung Luas Lingkaran\n","3. Menghitung Luas Segitiga\n","1\n","Menghitung Luas Persegi\n","Rumus = sisi x sisi\n","masukan sisi :6\n","Luas Perseginya adalah : 36\n"]}]}]}