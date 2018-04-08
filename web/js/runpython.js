$.ajax({
  type: "POST",
  url: "/hello.py",
  data: { param: text}
}).done(function( o ) {
   // do something
});
