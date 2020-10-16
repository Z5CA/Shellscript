cat $1 |  grep "^ " | cut -d$'\t' -f 2 | tr '\n' ' ' | sed -e 's/ *$//' | sed -e 's/ \+/\\x/g'| awk '{print "\\x"$0}'
