document.addEventListener("DOMContentLoaded", () => {
    let docTitle = document.title;
    
    document.addEventListener("visibilitychange", () => {
        if (document.hidden) {
            document.title = "Come Back :(";
        } else {
            document.title = docTitle;
        }
    });
});