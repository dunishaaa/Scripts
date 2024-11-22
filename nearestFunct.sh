#!/bin/bash


function get_scene(){

    declare -A line_matches

    file=$1
    line=$2
    nearest=100000
    scene=""

    while IFS=: read -r line_number match; do
        line_matches["$line_number"]="$match"
    done < <(grep -noh "\w*(Scene)" $file)

    for line_number in "${!line_matches[@]}"; do
        line_matches[$line_number]=$(echo ${line_matches[$line_number]} | sed 's/(Scene)//')
        cur=$(( $line - $line_number))
        if [ $cur -ge 0 ]; then
            if [ $cur -le $nearest ]; then
                echo $cur
                nearest=$cur
                scene=${line_matches[$line_number]}
            fi
        fi
    done
    echo "Nearest function -> $scene"

}

get_scene $1 $2
