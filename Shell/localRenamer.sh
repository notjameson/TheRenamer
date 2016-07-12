# Created by Jameson Zaballos, 2016. Please don't mess around with this.
IFS=$(echo -en "\n\b")
#!/bin/bash
echo "Beginning renaming files..."
for file in *;


do 
# Check the size of the file to determine where to cocatenate for .jpg extension
size=${#file}

lessSize=`expr $size - 3`

# Set "check" variable to determine if the extension is .jpg (and we can start)
check=${file:$lessSize:$size}

# If that works, keep going...
if [ "$check" == "jpg" ]
	then
	# Set the start of the new SKU ID, cutting off the .jpg ending with the next expression
	end=`expr $size - 10`
	lessSize=`expr $size - 10`

	# Grab the six digit part of the SKU
	newFile=${file:$lessSize:6}
	echo "This is the 6-digit part of the SKU: $newFile"

	# Get the one-digit SKU
	newSkuStart=`expr $size - 12`
	startFile=${file:$newSkuStart:1}
	echo "This is the letter tag of the SKU: $startFile"

	newFile="$newFile"_"$startFile".jpg
	printf '%s\n' "${f%.shp}$newFile"
	mv -n "$file" $newFile
fi
done