#!bin/bash
echo "Iniciando o Script para monitoramento do processo phyton indicado no arquivo pid"

while true
	do
	file="pid"
	while IFS= read -r line
		do
		ps "$line" && echo "1: It is alive" || (echo "1: It is dead" &&  ./script.py  && sleep 4)
		done < "file"

	sleep 4
done

