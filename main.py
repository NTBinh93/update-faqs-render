import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def update_faqs():
    conn = psycopg2.connect(
        host="dpg-d06q1dbuibrs73er06gg-a.render.com",  # CHÚ Ý: internal hostname
        port=5432,
        database="chatbotbvagdb",
        user="chatbotbvaguser",
        password="lwVzu89VrUY1NHPakyij94D3JJUz9QO5"
    )
    cur = conn.cursor()

    cur.execute("DELETE FROM faqs")

    data = [
        ("Ngoại trú được bảo hiểm những chi phí nào?, Ngoại trú là gì?., Ngoại trú được chi trả những chi phí nào?, Ngoại trú có những quyền lợi gì?, Ngoại trú là quyền lợi gì? ",
     "Ngoại trú là một quyền lợi tùy chọn mua thêm, đây là một hình thức điều trị y tế mà bệnh nhân không cần phải nằm viện qua đêm hay trong thời gian dài. Thay vào đó, bệnh nhân có thể đến cơ sở y tế, nhận dịch vụ chăm sóc hoặc điều trị cần thiết nhưng không phải làm thủ tục nhập viện và sau đó trở về nhà trong cùng ngày. Ngoại trú chi trả chi phí khám bệnh, xét nghiệm, chẩn đoán hình ảnh, thuốc theo toa, phẫu thuật ngoại trú, vật lý trị liệu theo chỉ định của bác sĩ... Nói cách khác, ngoại trú là việc điều trị y tế tại một cơ sở y tế/bệnh viện/phòng khám nhưng không nhập viện điều trị nội trú. Các trường hợp điều trị trong ngày, phẫu thuật/tiểu phẫu/nội soi chẩn đoán bệnh trong ngày được giải quyết theo quyền lợi điều trị ngoại trú"),

    ("Bảo hiểm Nha khoa chi trả những chi phí nào?., Quyền lợi nha khoa được chi trả gì?, Bảo hiểm nha khoa có những quyền lợi gì?",
     "quyền lợi Nha khoa bao gồm chi phí điều trị nha khoa như lấy cao răng, trám răng, nhổ răng, chữa tủy răng, điều trị viêm nướu, viêm nha chu... Đây là quyền lợi tùy chọn mua thêm, bạn có thể yêu cầu 'tham khảo quyền lợi bảo hiểm' để xem bảng minh họa chi tiết hơn"),

    ("Bảo hiểm Thai sản chi trả cho những trường hợp nào?., thai sản được trả chi phí gì?, Bảo hiểm thai sản chi trả như thế nào?",
     "bảo hiểm thai sản chi trả cho sinh thường, sinh mổ theo chỉ định của bác sĩ, biến chứng thai sản, chăm sóc trước và sau sinh. Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sinh nở cần đến các thủ thuật sản khoa, chi phí chăm sóc mẹ trước và sau khi sinh tại bệnh viện. Thủ thuật sinh mổ chỉ được bảo hiểm nếu do bác sĩ chỉ định là cần thiết cho ca sinh đó, không bao gồm việc sinh mổ theo yêu cầu (hoặc phải mổ lại do việc yêu cầu mổ trước đó). Đối với sinh thường Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợp, bác sĩ chuyên khoa, chăm sóc mẹ trước và sau khi sinh tại bệnh viện, chi phí may thẩm mỹ đường rạch"),

    ("Tai nạn cá nhân được chi trả cho trường hợp nào?., Bảo hiểm tai nạn cá nhân chi trả như thế nào?, Tai nạn cá nhân có quyền lợi gì?, Tai nạn cá nhân là quyền lợi gì?, quyền lợi tai nạn cá nhân là gì?, quyền lợi bảo hiểm tai nạn cá nhân là gì?",
     "bảo hiểm tai nạn cá nhân là một quyền lợi tùy chọn mua thêm, chi trả cho trường hợp tử vong, thương tật toàn bộ vĩnh viễn hoặc thương tật bộ phận vĩnh viễn (ví dụ mất một ngón tay, mắt...) do tai nạn xảy ra trong thời hạn bảo hiểm. Trường hợp Người được bảo hiểm chết hoặc thương tật toàn bộ vĩnh viễn do tai nạn thuộc phạm vi bảo hiểm, Bảo hiểm Bảo Việt trả toàn bộ số tiền bảo hiểm trên Giấy chứng nhận bảo hiểm hoặc Hợp đồng bảo hiểm. Trường hợp Người được bảo hiểm bị thương tật bộ phận vĩnh viễn do tai nạn thuộc phạm vi bảo hiểm, Bảo hiểm Bảo Việt trả theo Phụ lục Bảng tỷ lệ trả tiền thương tật quy định trong hợp đồng/ Quy tắc bảo hiểm. Trường hợp Người được bảo hiểm bị tai nạn dẫn đến thương tật bộ phận vĩnh viễn đã được trả tiền bảo hiểm, trong vòng 365 ngày kể từ ngày xảy ra tai nạn Người được bảo hiểm bị chết do hậu quả của chính tai nạn đó, Bảo hiểm Bảo Việt sẽ trả phần chênh lệch giữa số tiền bảo hiểm ghi trong Hợp đồng hoặc Giấy chứng nhận bảo hiểm với số tiền đã trả trước đó"),

    ("Sinh mạng cá nhân được chi trả trong những trường hợp nào?., Bảo hiểm sinh mạng cá nhân chi trả như thế nào?, Sinh mạng cá nhân có quyền lợi gì?, Sinh mạng cá nhân là quyền lợi gì?, quyền lợi sinh mạng cá nhân là gì?, quyền lợi bảo hiểm sinh mạng cá nhân là gì?",
     "bảo hiểm sinh mạng cá nhân là một quyền lợi tùy chọn mua thêm, chi trả trong trường hợp tử vong hoặc thương tật toàn bộ vĩnh viễn không do tai nạn. Trường hợp Người được bảo hiểm chết hoặc tàn tật toàn bộ vĩnh viễn thuộc phạm vi bảo hiểm, Bảo hiểm Bảo Việt trả toàn bộ số tiền bảo hiểm ghi trên Giấy chứng nhận bảo hiểm hoặc Hợp đồng bảo hiểm"),

    ("tôi muốn mua bảo hiểm thai sản., tôi muốn mua bảo hiểm thai sản thì cần điều kiện gì?, bảo hiểm thai sản trả những chi phí nào?, bảo hiểm thai sản có quyền lợi gì?",
     "bảo hiểm thai sản áp dụng cho nữ độ tuổi từ 18 đến 45, đây là một quyền lợi bổ sung, tùy chọn mua thêm, vì vậy, mình phải chọn tham gia tối thiểu quyền lợi chính 'Điều trị Nội trú do ốm bệnh, tai nạn', sau đó mình được quyền mua tiếp quyền lợi phụ/bổ sung thai sản. Quyền lợi thai sản áp dụng từ chương trình Bạc trở lên, và bạn cần tham gia liên tục ít nhất 2 năm để qua thời gian chờ là 635 ngày nhé. Sau khi qua thời gian chờ này, mình bắt đầu sinh con sẽ được bảo hiểm cho trường hợp sinh thường hoặc sinh mổ theo chỉ định của bác sĩ, biến chứng thai sản, chăm sóc trước và sau sinh. Bảo hiểm Bảo Việt sẽ chi trả các chi phí y tế phát sinh do các biến chứng trong quá trình mang thai, hoặc trong quá trình sinh nở cần đến các thủ thuật sản khoa, chi phí chăm sóc mẹ trước và sau khi sinh tại bệnh viện. Thủ thuật sinh mổ chỉ được bảo hiểm nếu do bác sĩ chỉ định là cần thiết cho ca sinh đó, không bao gồm việc sinh mổ theo yêu cầu (hoặc phải mổ lại do việc yêu cầu mổ trước đó). Đối với sinh thường Bảo Việt sẽ chi trả các chi phí y tế phát sinh cho việc Sinh thường bao gồm và không giới hạn trong các chi phí: đỡ đẻ, viện phí tổng hợp, bác sĩ chuyên khoa, chăm sóc mẹ trước và sau khi sinh tại bệnh viện, chi phí may thẩm mỹ đường rạch. <br>👉 Nếu bạn chỉ muốn mua bảo hiểm thai sản, em sẽ gửi thông tin chi tiết, hãy nhập thêm độ tuổi, ví dụ: <br><b>💡 bảo hiểm thai sản 28 tuổi"),

    ("đồng chi trả là gì?., đồng bảo hiểm là gì?",
     "đồng chi trả là tỷ lệ chi phí thuộc phạm vi bảo hiểm mà Người được bảo hiểm phải tự thanh toán khi khám chữa bệnh, áp dụng cho trẻ dưới 3 tuổi và các bệnh đặc biệt. Ví dụ, chi phí thuộc phạm vi bảo hiểm là 1 triệu đồng, áp dụng đồng bảo hiểm 20%, như vậy nghĩa là bạn sẽ tự trả 200 nghìn đồng, Bảo Việt sẽ chi trả 800 nghìn đồng"),

    ("bệnh ung thư có được bảo hiểm không?., Ung thư có chi trả không?, bệnh ung thư có được chi trả không?",
     "trong sản phẩm bảo hiểm Bảo Việt An Gia hiện tại, bệnh ung thư chưa nằm trong danh sách được bảo hiểm chi trả, do thuộc danh mục loại trừ số 12 của quy tắc bảo hiểm này"),

    ("Nằm viện là gì? nội trú là gì?. Chi phí nằm viện nào được bảo hiểm chi trả?, nội trú được chi trả những chi phí nào?, nội trú chi trả những chi phí nào?, Nội trú là quyền lợi gì? Nội trú có những quyền lợi gì?",
     "nằm viện nội trú là việc bệnh nhân phải lưu trú tại bệnh viện ít nhất là 24 giờ để điều trị. Trong trường hợp bệnh viện không cấp được Giấy nhập viện hoặc xuất viện, hồ sơ y tế hoặc hóa đơn thanh toán thể hiện rõ thời gian điều trị sẽ được coi như chứng từ thay thế. Đơn vị ngày nằm viện được tính bằng 24h và theo đơn vị giường nằm trong Giấy ra/xuất viện hoặc trong chứng từ viện phí chi tiết. Việc điều trị nội trú chỉ được chấp nhận khi bệnh nhân được thực hiện điều trị tại một bệnh viện như định nghĩa, không phải là phòng khám hay cơ sở điều trị ngoại trú. Bảo hiểm Bảo Việt sẽ thanh toán các chi phí điều trị, tiền phòng và giường, tiền ăn theo tiêu chuẩn điều trị nội trú của bệnh viện (nếu có), chi phí xét nghiệm, hoặc các phương pháp chẩn đoán hình ảnh như X-quang, MRI, CT, PET, siêu âm, nội soi (các xét nghiệm này phải do bác sỹ chỉ định là biện pháp cần thiết để đánh giá tình trạng bệnh và phải là một phần của chi phí điều trị nằm viện), thuốc điều trị, truyền máu, ô xy, huyết thanh, quần áo bệnh viện và các chi phí y tế liên quan khác nhưng tối đa không quá giới hạn phụ cho mỗi ngày điều trị quy định trong Bảng quyền lợi hoặc Giấy chứng nhận bảo hiểm"),

    ("Phẫu thuật được chi trả những chi phí nào?., Phẫu thuật có những loại nào?, Phẫu thuật được bảo hiểm những chi phí nào?, phẫu thuật trả những chi phí nào?, Phẫu thuật có quyền lợi gì?, Phẫu thuật chi trả những chi phí nào?",
     "trường hợp Người được bảo hiểm phải phẫu thuật phải nằm viện điều trị nội trú thuộc phạm vi bảo hiểm, Bảo hiểm Bảo Việt sẽ thanh toán toàn bộ các chi phí hội chẩn, gây mê, hồi sức, chi phí phẫu thuật bao gồm cả phẫu thuật cấy ghép nội tạng (không bảo hiểm cho chi phí mua các bộ phận nội tạng và chi phí hiến nội tạng). Giới hạn số tiền chi trả cho trường hợp phẫu thuật không vượt mức giới hạn tối đa do Người được bảo hiểm lựa chọn khi tham gia bảo hiểm và được ghi cụ thể trong Giấy chứng nhận bảo hiểm hoặc Hợp đồng bảo hiểm. Có 2 loại phẫu thuật là 'Phẫu thuật nội trú: là hình thức bệnh nhân sau phẫu thuật cần phải lưu trú tại bệnh viện ít nhất 24h' và 'Phẫu thuật ngoại trú: là hình thức bệnh nhân sau phẫu thuật chỉ lưu trú tại bệnh viện dưới 24h'"),

    ("Bệnh có sẵn là gì?, thương tật có sẵn là gì?.",
     "bệnh/thương tật có sẵn là gì là bệnh hoặc thương tật có từ trước ngày bắt đầu được nhận bảo hiểm theo hợp đồng bảo hiểm và là bệnh/thương tật mà Người được bảo hiểm: a. Đã phải điều trị trong vòng 03 năm gần đây; b. Là bất cứ tình trạng sức khỏe đã được chẩn đoán; triệu chứng bệnh/thương tật đã xảy ra/xuất hiện trước ngày ký hợp đồng mà Người được bảo hiểm đã biết hoặc ý thức được cho dù Người được bảo hiểm có thực sự khám, điều trị hay không"),

    ("liên hệ tư vấn viên như thế nào?. Tôi có thể liên hệ tư vấn viên ở đâu?",
     "nếu bạn cần hỗ trợ trực tiếp, đừng ngần ngại nhấn nút '📞 Liên hệ tư vấn viên' ở khung chat nhé. Hoặc bạn có thể liên hệ trực tiếp đến Mr. Nguyễn Thanh Bình – Bảo Việt TP.HCM qua số 0962.943.831 (Zalo/Viber). Anh Bình sẽ hỗ trợ bạn tận tình, kể cả khi bạn chưa rõ nên chọn gói nào, giúp bạn hoàn thành thủ tục cấp hợp đồng và đồng hành hỗ trợ bạn trong suốt quá trình sử dụng bảo hiểm hiệu quả"),

    (
        "Bệnh đặc biệt là gì?, Bệnh đặc biệt bao gồm những bệnh nào?",
        "theo Quy tắc bảo hiểm của sản phẩm này, những bệnh sau đây được hiểu là bệnh đặc biệt, bạn có thể tham khảo chi tiết trong danh mục bệnh đặc biệt đính kèm\n"
        "📄 Tải chi tiết định nghĩa: [Xem file PDF](static/images/benh_dac_biet.jpg)"
    ),
    (
        "Bệnh liệt kê là gì?",
        " tại điều khoản loại trừ số 36 liệt kê các bệnh không được bảo hiểm trong năm đầu tiên, bạn có thể tham khảo chi tiết danh mục bệnh trong tài liệu đính kèm dưới đây\n"
        "📄 Tải chi tiết: [Điều khoản loại trừ số 36](static/images/dieu_khoan_loai_tru_36.jpg)"
    )
    ]

    cur.executemany("INSERT INTO faqs (question, answer) VALUES (%s, %s)", data)

    conn.commit()
    cur.close()
    conn.close()

    return "✅ Cập nhật FAQs thành công!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
