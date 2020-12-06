function getInput(funzione){
	document.getElementById('inputfile')
		.addEventListener('change', function() {

			var fr=new FileReader();
			fr.onload=function(){
				input=fr.result;
				funzione()
			}

			fr.readAsText(this.files[0]);
		})
}

let nav="<li><a href=\"day1.html\">Day 1 </a></li>\n" +
	"\t<li><a href=\"day2.html\">Day 2 </a></li>\n" +
	"\t<li><a href=\"day3.html\">Day 3 </a></li>\n" +
	"\t<li><a href=\"day4.html\">Day 4 </a></li>\n" +
	"\t<li><a href=\"day5.html\">Day 5 </a></li>\n" +
	"\t<li><a href=\"day6.html\">Day 6 </a></li>"

function setUpNav(mobile, nonmobile){
	nonmobile.html(nav)
	mobile.html(nav)
}