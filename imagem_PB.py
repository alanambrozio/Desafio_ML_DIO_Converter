def converter_bmp_para_cinza(input_file, output_file):
    try:
        # Tenta abrir o arquivo de entrada
        with open(input_file, "rb") as f:
            print(f"Imagem '{input_file}' carregada com sucesso!")
            
            # Ler o cabeçalho do BMP
            header = f.read(54)
            
            width = int.from_bytes(header[18:22], byteorder="little")
            height = int.from_bytes(header[22:26], byteorder="little")
            
            # Ler os dados de pixel
            # Os dados são organizados em linhas, cada uma alinhada a múltiplos de 4 bytes
            row_size = (width * 3 + 3) & ~3  # Largura ajustada para alinhamento
            pixel_data = []
            for _ in range(height):
                row = f.read(row_size)
                pixel_data.append(row[:width * 3])  # Apenas os dados de pixel RGB

        # Converter os pixels para tons de cinza
        new_pixel_data = bytearray()
        for row in pixel_data:
            new_row = bytearray()
            for i in range(0, len(row), 3):
                b, g, r = row[i:i+3]
                gray = int(0.3 * r + 0.59 * g + 0.11 * b)  # Fórmula para tons de cinza
                new_row.extend([gray, gray, gray])  # Mesma intensidade para R, G, B
            # Preencher o alinhamento
            padding = (row_size - width * 3)
            new_row.extend([0] * padding)
            new_pixel_data.extend(new_row)

        # Escrever os dados no arquivo de saída
        with open(output_file, "wb") as f:
            f.write(header)  # Escrever o cabeçalho original
            f.write(new_pixel_data)  # Escrever os novos pixels
        
        print(f"Imagem convertida com sucesso e salva como '{output_file}'!")

    except FileNotFoundError:
        print(f"Arquivo '{input_file}' não encontrado. Verifique o nome e a localização.")
    except ValueError as e:
        print(f"Erro no processamento: {e}")

# Exemplo de uso
converter_bmp_para_cinza("yennefer.bmp", "imagem_cinza.bmp")

def converter_bmp_para_pb(input_file, output_file):
    try:
        # Tenta abrir o arquivo de entrada
        with open(input_file, "rb") as f:
            print(f"Imagem '{input_file}' carregada com sucesso!")
            
            # Ler o cabeçalho do BMP
            header = f.read(54)
            
            width = int.from_bytes(header[18:22], byteorder="little")
            height = int.from_bytes(header[22:26], byteorder="little")
            
            # Ler os dados de pixel
            # Os dados são organizados em linhas, cada uma alinhada a múltiplos de 4 bytes
            row_size = (width * 3 + 3) & ~3  # Largura ajustada para alinhamento
            pixel_data = []
            for _ in range(height):
                row = f.read(row_size)
                pixel_data.append(row[:width * 3])  # Apenas os dados de pixel RGB

        # Converter os pixels para tons de cinza
        new_pixel_data = bytearray()
        for row in pixel_data:
            new_row = bytearray()
            for i in range(0, len(row), 3):
                r, g, b = row[i], row[i + 1], row[i + 2]  # Tons de cinza
                gray = r  # R, G, B são iguais em imagens cinza
                if gray < 165:
                    new_row.extend([0, 0, 0])  # Preto
                else:
                    new_row.extend([255, 255, 255])  # Branco
            # Preencher o alinhamento
            padding = (row_size - width * 3)
            new_row.extend([0] * padding)
            new_pixel_data.extend(new_row)

        # Escrever os dados no arquivo de saída
        with open(output_file, "wb") as f:
            f.write(header)  # Escrever o cabeçalho original
            f.write(new_pixel_data)  # Escrever os novos pixels
        
        print(f"Imagem convertida com sucesso e salva como '{output_file}'!")

    except FileNotFoundError:
        print(f"Arquivo '{input_file}' não encontrado. Verifique o nome e a localização.")
    except ValueError as e:
        print(f"Erro no processamento: {e}")

# Exemplo de uso
converter_bmp_para_pb("imagem_cinza.bmp", "imagem_PB.bmp")